from pydio.api import Injector, Provider

from src.domains.teams import commands, gateways, interfaces, queries
from src.gateways.storage import IStorageAggregate
from src.gateways.teams.storage import DatabaseTeamsStorage

provider = Provider()


@provider.provides(gateways.ITeamsStorage, scope="app")
async def make_team_storage(injector: Injector):
    return DatabaseTeamsStorage(
        await injector.inject(IStorageAggregate.IStorageSession)
    )


@provider.provides(interfaces.ICreateTeam, scope="app")
async def build_create_team_command(injector: Injector):
    storage = await injector.inject(gateways.ITeamsStorage)
    return commands.CreateTeam(storage)


@provider.provides(interfaces.IDeleteTeam, scope="app")
async def build_delete_team_command(injector: Injector):
    storage = await injector.inject(gateways.ITeamsStorage)
    return commands.DeleteTeam(storage)


@provider.provides(interfaces.IFetchAllTeams, scope="app")
async def build_fetch_all_teams_command(injector: Injector):
    storage = await injector.inject(gateways.ITeamsStorage)
    return queries.FetchAllTeams(storage)


@provider.provides(interfaces.IEditTeam, scope="app")
async def build_edit_team_command(injector: Injector):
    storage = await injector.inject(gateways.ITeamsStorage)
    return commands.EditTeam(storage)
