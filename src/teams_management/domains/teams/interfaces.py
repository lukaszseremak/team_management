import abc
from typing import List
from uuid import UUID

from pydantic import BaseModel

from teams_management.domains.teams import entities


class TeamNotFound(BaseException):  # noqa: WPS418
    def __init__(self):
        super().__init__("Team not found")


class ICreateTeam(abc.ABC):
    class Args(BaseModel):
        req: entities.CreateTeamRequest

    class Result(entities.Team):
        pass

    @abc.abstractmethod
    async def invoke(self, args: Args) -> Result:
        pass


class IDeleteTeam(abc.ABC):
    class Args(BaseModel):
        uid: UUID

    class Result(BaseModel):
        success: bool

    @abc.abstractmethod
    async def invoke(self, args: Args) -> Result:
        pass


class IEditTeam(abc.ABC):
    class Args(BaseModel):
        req: entities.EditTeamRequest

    class Result(BaseModel):
        success: bool
        team: entities.Team

    @abc.abstractmethod
    async def invoke(self, args: Args) -> Result:
        pass


class IFetchAllTeams(abc.ABC):
    class Result(List[entities.Team]):
        pass

    @abc.abstractmethod
    async def invoke(self) -> Result:
        pass
