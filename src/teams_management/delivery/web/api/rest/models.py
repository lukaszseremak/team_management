from pydantic import BaseModel


class CreateTeamRequest(BaseModel):
    name: str


class DeleteResponse(BaseModel):
    success: bool


class EditTeamRequest(BaseModel):
    name: str


class Team(BaseModel):
    uid: str
    name: str
