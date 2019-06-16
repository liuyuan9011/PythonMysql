#-*- coding:utf-8 -*-

from sqlalchemy.engine import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from const import *

import logging

PGCReadOnlySession = scoped_session(sessionmaker())
PGCSession = scoped_session(sessionmaker())


def make_mysql_engine(host, port, user, passwd, db, read_timeout, read_only=False, **kwargs):
    options = {
        'connect_timeout': 1, 'read_timeout': read_timeout,
    }
    if read_only:
        options['autocommit'] = 1
    if port:
        engine = create_engine('%s://%s:%s@%s:%s/%s?charset=utf8&use_unicode=1' % ("mysql", user, passwd, host, port, db),
            pool_recycle=30,
            connect_args=options,
            **kwargs
        )
    else:
        engine = create_engine('%s://%s:%s@%s/%s?charset=utf8&use_unicode=1' % ("mysql", user, passwd, host, db),
            pool_recycle=30,
            connect_args=options,
            **kwargs
        )
    return engine


def config_pgcdb_read_session(conf, read_timeout=DEFAULT_READ_TIMEOUT, echo=False):
    try:
        engine = make_mysql_engine(
            conf.host, conf.port,
            conf.user, conf.password,
            conf.db_name, read_timeout, True, echo=echo, poolclass=NullPool)
        PGCReadOnlySession.configure(bind=engine, autoflush=False, autocommit=True, expire_on_commit=False)
    except:
        logging.exception('pgcdb read session configuration failed')


def config_pgcdb_write_session(conf, read_timeout=DEFAULT_READ_TIMEOUT, echo=False):
    try:
        engine = make_mysql_engine(
            conf.host, conf.port,
            conf.user, conf.password,
            conf.db_name, read_timeout, True, echo=echo, poolclass=NullPool)
        PGCSession.configure(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    except:
        logging.exception('pgcdb read session configuration failed')


def raw_session():
    config_pgcdb_read_session(DB_CONF)
    g_session = PGCReadOnlySession()
    return g_session


def raw_w_session():
    config_pgcdb_write_session(DB_CONF)
    g_session = PGCSession()
    return g_session


def get_session(write=False):
    if write:
        print('Write Session')
        h = raw_w_session()
    else:
        h = raw_session()
    return h


