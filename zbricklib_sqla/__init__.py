from flask import Flask
from zbricklib.extension import zExtension  # type: ignore[import]

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, inspect
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class zSQLAlchemy(SQLAlchemy, zExtension):
    _ext_name = 'sqla'

    def __init__(self, *args, **kwargs):
        SQLAlchemy.__init__(self, *args, model_class=Base, **kwargs)
        zExtension.__init__(self, *args, **kwargs)

    def init_app(self, app: Flask):
        zExtension.init_app(self, app)

    def _install_into(self, app: Flask):
        SQLAlchemy.init_app(self, app)

sqla = zSQLAlchemy()

__all__ = [
    'sqla', 
    'zSQLAlchemy', 'Base'
    'Mapped', 'mapped_column',
    'select', 'inspect',
]