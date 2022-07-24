from src.domains.teams import gateways, interfaces


class FetchAllTeams(interfaces.IFetchAllTeams):
    def __init__(self, storage: gateways.ITeamsStorage):
        self._storage = storage

    async def invoke(self):
        result = await self._storage.fetch_all()
        return sorted(result, key=lambda elem: elem.name)
