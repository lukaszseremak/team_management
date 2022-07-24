import abc
from contextlib import asynccontextmanager
from enum import Enum
from typing import AsyncIterator


class IsolationLevel(Enum):
    READ_COMMITTED = 1  # noqa: WPS115
    REPEATABLE_READ = 2  # noqa: WPS115
    SERIALIZABLE = 3  # noqa: WPS115


class IStorageAggregate(abc.ABC):
    class IStorageSession(abc.ABC):
        @asynccontextmanager  # type: ignore
        @abc.abstractmethod
        async def begin_db_session(self) -> None:
            pass

    @abc.abstractmethod
    def create_session(self) -> IStorageSession:
        pass

    @asynccontextmanager  # type: ignore
    @abc.abstractmethod
    async def acquire_session(self) -> AsyncIterator[IStorageSession]:
        pass

    @asynccontextmanager  # type: ignore
    @abc.abstractmethod
    async def acquire_transactional_session(self, **kwargs) -> AsyncIterator[IStorageSession]:
        pass
