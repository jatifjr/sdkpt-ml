from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # generate tablename automatically if not declared
    @declared_attr
    def __tablename__(cls) -> str:
        if not hasattr(cls, '__tablename__'):
            return cls.__name__.lower()
        return cls.__tablename__
