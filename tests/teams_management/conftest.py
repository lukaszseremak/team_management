import pytest
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy_utils.functions import create_database, database_exists
from starlette.testclient import TestClient

from src.teams_management.delivery.config import config as web_config
from src.teams_management.delivery.web.app import create_app
from src.teams_management.gateways.database.base import Base, init_db_engine

from .helpers.communication import rest


@pytest.fixture(name="database_engine", scope="session")
def make_database_engine():
    url = web_config.DATABASE_URL

    if not database_exists(url):
        create_database(url)

    return init_db_engine(url)


@pytest.fixture
def client(database_engine):
    app = create_app()
    app.debug = True

    Base.metadata.create_all(bind=database_engine)
    try:
        with TestClient(app) as test_client:
            yield rest.APIClient(test_client)
    finally:
        close_all_sessions()
        Base.metadata.drop_all(bind=database_engine)
