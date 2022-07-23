from pydio.api import Provider

from src.delivery.config import Config
from src.delivery.config import config as web_config

from .database import provider as database_provider


def build_factory():
    core_provider = Provider()
    core_provider.register_instance(Config, web_config, scope="app")

    factory = Provider()
    factory.attach(core_provider)
    factory.attach(database_provider)

    return factory
