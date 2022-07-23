from pydio.api import Injector, Provider
from sqlalchemy.orm import Session as AlchemyDatabase

from src.delivery.config import Config
from src.gateways.database.base import StorageAggregate, init_db_engine
from src.gateways.storage import IStorageAggregate

provider = Provider()


@provider.provides(AlchemyDatabase, scope='app')
async def connect(injector: Injector):
    config = injector.inject(Config)

    engine = init_db_engine(config.DATABASE_URL)
    return AlchemyDatabase(engine)


@provider.provides(IStorageAggregate.IStorageSession, scope='app')
async def make_storage_session(injector: Injector):
    return StorageAggregate.Session(await injector.inject(AlchemyDatabase))
