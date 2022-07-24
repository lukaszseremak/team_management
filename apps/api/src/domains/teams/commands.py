from src.domains.teams import gateways, interfaces
from src.domains.teams.gateways import NotFound


class CreateTeam(interfaces.ICreateTeam):
    def __init__(self, storage: gateways.ITeamsStorage):
        self._storage = storage

    async def invoke(self, args):
        result = await self._storage.create(name=args.req.name)
        return result


class EditTeam(interfaces.IEditTeam):
    def __init__(self, storage: gateways.ITeamsStorage):
        self._storage = storage

    async def invoke(self, args):
        try:
            result = await self._storage.edit(uid=args.req.uid, name=args.req.name)
        except NotFound:
            raise interfaces.TeamNotFound()
        return result


class DeleteTeam(interfaces.IDeleteTeam):
    def __init__(self, storage: gateways.ITeamsStorage):
        self._storage = storage

    async def invoke(self, args):
        try:
            success = await self._storage.delete(uid=args.uid)
        except NotFound:
            raise interfaces.TeamNotFound()
        return self.Result(success=success)
