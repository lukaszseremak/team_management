from uuid import UUID

from pydantic import BaseModel


class Team(BaseModel):
    uid: UUID
    name: str


class CreateTeamRequest(BaseModel):
    name: str


class EditTeamRequest(BaseModel):
    name: str
    uid: UUID
