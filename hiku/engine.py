from functools import partial
from itertools import chain
from collections import defaultdict

from .edn import Keyword, Dict
from .graph import Link, Edge
from .store import Store
from .reader import read


def edge_split(edge, pattern):
    fields = []
    links = []

    for item in pattern:
        if isinstance(item, Keyword):
            fields.append(edge.fields[item])
        elif isinstance(item, Dict):
            for key, value in item.items():
                field = edge.fields[key]
                if isinstance(field, Link):
                    if field.requires:
                        fields.append(edge.fields[field.requires])
                    links.append((field, value))
                elif isinstance(field, Edge):
                    _fields, _links = edge_split(field, value)
                    fields.extend(_fields)
                    links.extend(_links)
                else:
                    raise ValueError('Unexpected name: {}'.format(key))
        else:
            raise ValueError('Unexpected value: {!r}'.format(item))

    return fields, links


def store_fields(store, edge, fields, ids, result):
    names = [f.name for f in fields]
    if edge.name is not None:
        if ids is not None:
            for i, row in zip(ids, result):
                store[edge.name][i].update(zip(names, row))
        else:
            store[edge.name].update(zip(names, result))
    else:
        store.update(zip(names, result))


def link_reqs(store, edge, link, ids):
    if edge.name is not None:
        if ids is not None:
            return [store[edge.name][i][link.requires] for i in ids]
        else:
            return store[edge.name][link.requires]
    else:
        return store[link.requires]


def link_ref(store, link, ident):
    return store.ref(link.entity, ident)


def link_refs(store, link, idents):
    return [store.ref(link.entity, i) for i in idents]


def store_links(store, edge, link, ids, result):
    field_val = partial(link_refs if link.to_list else link_ref,
                        store, link)
    if edge.name is not None:
        if ids is not None:
            for i, res in zip(ids, result):
                store[edge.name][i][link.name] = field_val(res)
        else:
            store[edge.name][link.name] = field_val(result)
    else:
        store[link.name] = field_val(result)


def link_result_to_ids(is_list, to_list, result):
    if is_list and to_list:
        return list(chain.from_iterable(result))
    elif is_list or to_list:
        return result
    else:
        return [result]


def _process_wait_list(wait_list, futures):
    for fut_set, callback in wait_list:
        fut_set.difference_update(futures)
        if fut_set:
            yield fut_set, callback
        else:
            callback()


class Query(object):

    def __init__(self, executor, root, pattern):
        self.executor = executor
        self.root = root
        self.pattern = pattern

        self.store = Store()
        self.futures = set()
        self._wait_list = []

    def begin(self):
        self._process_edge(self.root, self.pattern, None)

    def _submit(self, fn, *args):
        fut = self.executor.submit(fn, *args)
        self.futures.add(fut)
        return fut

    def _wait(self, futures, callback):
        self._wait_list.append((set(futures), callback))

    def progress(self, futures):
        self._wait_list = list(_process_wait_list(self._wait_list, futures))
        self.futures.difference_update(futures)

    def result(self):
        return self.store

    def _process_edge(self, edge, pattern, ids):
        fields, links = edge_split(edge, pattern)

        to_func = {}
        from_func = defaultdict(list)
        for field in fields:
            to_func[field.name] = field.func
            from_func[field.func].append(field.name)

        # schedule fields resolve
        to_fut = {}
        for func, names in from_func.items():
            if ids is not None:
                fut = self._submit(func, names, ids)
            else:
                fut = self._submit(func, names)
            to_fut[func] = fut
            self._wait([fut], (
                lambda _fut=fut:
                store_fields(self.store, edge, fields, ids, _fut.result())
            ))

        # schedule link resolve
        for link, link_pattern in links:
            if link.requires:
                fut = to_fut[to_func[link.requires]]
                self._wait([fut], (
                    lambda:
                    self._process_edge_link(edge, link, link_pattern, ids)
                ))
            else:
                fut = self._submit(link.func)
                self._wait([fut], (
                    lambda _fut=fut:
                    self._process_link(edge, link, link_pattern, ids,
                                       _fut.result())
                ))

    def _process_edge_link(self, edge, link, link_pattern, ids):
        reqs = link_reqs(self.store, edge, link, ids)
        fut = self._submit(link.func, reqs)
        self._wait([fut], (
            lambda:
            self._process_link(edge, link, link_pattern, ids, fut.result())
        ))

    def _process_link(self, edge, link, link_pattern, ids, result):
        store_links(self.store, edge, link, ids, result)
        to_ids = link_result_to_ids(ids is not None, link.to_list, result)
        self._process_edge(self.root.fields[link.entity], link_pattern,
                           to_ids)


class Engine(object):

    def __init__(self, executor):
        self.executor = executor

    def execute(self, root, pattern):
        query = Query(self.executor, root, pattern)
        return self.executor.process(query)
