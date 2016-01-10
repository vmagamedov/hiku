from __future__ import absolute_import

from json import dumps as _dumps

from ..store import Ref


def default(obj):
    if isinstance(obj, Ref):
        return obj.storage[obj.entity][obj.ident]
    raise TypeError('Can not encode this type: {!r}'.format(obj))


def dumps(data):
    return _dumps(data, default=default)
