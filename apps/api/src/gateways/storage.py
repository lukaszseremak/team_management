import abc
from contextlib import asynccontextmanager
from enum import Enum
from typing import AsyncIterator


class IsolationLevel(Enum):
    READ_COMMITTED = 1
    REPEATABLE_READ = 2
    SERIALIZABLE = 3


class IStorageAggregate(abc.ABC):
    class IStorageSession(abc.ABC):
        @asynccontextmanager
        @abc.abstractmethod
        async def begin_db_session(self) -> None:
            pass

    @abc.abstractmethod
    def create_session(self) -> IStorageSession:
        pass

    @asynccontextmanager
    @abc.abstractmethod
    async def acquire_session(self) -> AsyncIterator[IStorageSession]:
        pass

    @asynccontextmanager
    @abc.abstractmethod
    async def acquire_transactional_session(self, **kwargs) -> AsyncIterator[IStorageSession]:
        pass
