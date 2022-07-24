import abc
from typing import List
from uuid import UUID

from src.teams_management.domains.teams import entities


class NotFoundError(Exception):
    pass


class ITeamsStorage(abc.ABC):
    @abc.abstractmethod
    async def create(self, name: str) -> entities.Team:
        pass

    @abc.abstractmethod
    async def delete(self, uid: UUID) -> bool:
        pass

    @abc.abstractmethod
    async def fetch_all(self) -> List[entities.Team]:
        pass

    @abc.abstractmethod
    async def edit(self, uid: UUID, name: str) -> entities.Team:
        pass
