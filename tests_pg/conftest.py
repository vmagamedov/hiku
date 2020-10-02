import uuid

import pytest
import sqlalchemy
import psycopg2.extensions

from tests.test_source_sqlalchemy import setup_db


@pytest.fixture(scope='session', name='db_dsn')
def db_dsn_fixture(request):
    name = 'test_{}'.format(uuid.uuid4().hex)
    pg_dsn = 'postgresql://postgres:postgres@postgres:5432/postgres'
    db_dsn = 'postgresql://postgres:postgres@postgres:5432/{}'.format(name)

    pg_engine = sqlalchemy.create_engine(pg_dsn)
    pg_engine.raw_connection()\
        .set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    pg_engine.execute('CREATE DATABASE {0}'.format(name))
    pg_engine.dispose()

    db_engine = sqlalchemy.create_engine(db_dsn)
    setup_db(db_engine)
    db_engine.dispose()

    def fin():
        pg_engine = sqlalchemy.create_engine(pg_dsn)
        pg_engine.raw_connection() \
            .set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        pg_engine.execute('DROP DATABASE {0}'.format(name))
        pg_engine.dispose()

    request.addfinalizer(fin)
    return db_dsn
