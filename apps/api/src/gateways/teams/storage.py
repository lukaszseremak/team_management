from typing import List
from uuid import UUID

from src.domains.teams import entities, gateways
from src.domains.teams.gateways import NotFound
from src.gateways.database import tables
from src.gateways.storage import IStorageAggregate


class DatabaseTeamsStorage(gateways.ITeamsStorage):
    def __init__(self, storage_session: IStorageAggregate.IStorageSession):
        self._storage_session = storage_session

    def _map_orm_to_entity(self, obj):
        return entities.Team(name=obj.name, uid=obj.uid)

    async def create(self, name: str):
        async with self._storage_session.begin_db_session() as db_session:
            obj = tables.Team(name=name)
            db_session.add(obj)
            db_session.commit()
            db_session.refresh(obj)

            return self._map_orm_to_entity(obj)

    async def delete(self, uid: UUID):
        async with self._storage_session.begin_db_session() as db_session:
            affected_rows = (
                db_session.query(tables.Team).filter(tables.Team.uid == uid).delete()
            )
            if affected_rows == 0:
                raise NotFound

            db_session.commit()
            return True

    async def fetch_all(self) -> List[entities.Team]:
        async with self._storage_session.begin_db_session() as db_session:
            teams = db_session.query(tables.Team).all()

            return [self._map_orm_to_entity(team) for team in teams]

    async def edit(self, uid: UUID, name: str) -> bool:
        async with self._storage_session.begin_db_session() as db_session:
            team = db_session.query(tables.Team).get(uid)
            if not team:
                raise NotFound("Team not found")
            team.name = name
            db_session.commit()
            return self._map_orm_to_entity(team)
