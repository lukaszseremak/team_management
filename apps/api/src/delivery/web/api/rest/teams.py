from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Request

from src.delivery.web.api.rest import models
from src.domains.teams import entities, interfaces

router = APIRouter()


def map_entity_to_api_model(entity: entities.Team):
    return models.Team(uid=str(entity.uid), name=entity.name)


@router.post("", response_model=models.Team, status_code=201)
async def create(data: models.CreateTeamRequest, request: Request):
    command = await request.app.injector.inject(interfaces.ICreateTeam)
    args = command.Args(req=data)
    result = await command.invoke(args)
    return map_entity_to_api_model(result)


@router.get("", response_model=List[models.Team], status_code=200)
async def get_all(request: Request):
    query = await request.app.injector.inject(interfaces.IFetchAllTeams)
    result = await query.invoke()
    return [map_entity_to_api_model(team) for team in result]


@router.delete("/{uid}", response_model=models.DeleteResponse, status_code=200)
async def delete(uid: UUID, request: Request):
    command = await request.app.injector.inject(interfaces.IDeleteTeam)
    args = command.Args(uid=uid)
    try:
        result = await command.invoke(args)
    except interfaces.TeamNotFound:
        raise HTTPException(status_code=404, detail=f"Record {uid} not found")
    return models.DeleteResponse(success=result.success)


@router.put("/{uid}", response_model=models.Team, status_code=200)
async def edit(uid: UUID, data: models.EditTeamRequest, request: Request):
    command = await request.app.injector.inject(interfaces.IEditTeam)
    args = command.Args(req={"uid": uid, "name": data.name})
    try:
        result = await command.invoke(args)
    except interfaces.TeamNotFound:
        raise HTTPException(status_code=404, detail=f"Record {uid} not found")
    return map_entity_to_api_model(result)
