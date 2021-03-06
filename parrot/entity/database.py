#!/usr/bin/env python3

import os

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


def __get_sqlalchemy_database_url() -> str:
    url = os.getenv("SQLALCHEMY_DATABASE_URL")
    assert url is not None
    return url


def get_engine() -> Engine:
    url = __get_sqlalchemy_database_url()
    connect_args = {}
    if url.lower().startswith("sqlite"):
        connect_args["check_same_thread"] = False
    return create_engine(url, connect_args=connect_args)


def get_local_session() -> Session:
    return sessionmaker(autocommit=False, autoflush=False, bind=get_engine())


ModelBase = declarative_base()
