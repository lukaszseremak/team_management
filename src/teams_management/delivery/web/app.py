from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from pydio.api import Injector

from src.teams_management.delivery.config import config as web_config
from src.teams_management.delivery.di import build_factory
from src.teams_management.delivery.web.api.rest import teams


def _register_routes(app):
    app.include_router(teams.router, prefix="/teams", tags=["Teams Tag"])


def _configure_dependency_injector(app):
    provider = build_factory()
    app.injector = Injector(provider).scoped("app", env=web_config.ENV)


def _configure_cors(app):
    front_url = "*"
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[front_url],
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_app():
    app = FastAPI(title="Teams Managment API")

    @app.get("/", include_in_schema=False)
    async def access_documentation():
        openapi_url = "/api/openapi.json"
        return get_swagger_ui_html(openapi_url=openapi_url, title="docs")

    @app.get("/api/openapi.json", include_in_schema=False)
    async def access_openapi():
        openapi = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
            tags=app.openapi_tags,
        )

        monkey_patched_openapi = {key: value for key, value in openapi.items() if key != "paths"}
        monkey_patched_openapi["paths"] = {}
        for key, value in openapi["paths"].items():
            print(app.root_path)  # noqa: WPS421
            monkey_patched_openapi["paths"][key] = value

        return monkey_patched_openapi

    _configure_dependency_injector(app)
    _register_routes(app)
    _configure_cors(app)

    return app
