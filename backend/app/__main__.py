from fastapi import FastAPI
from fastapi_pagination import add_pagination
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

from .config import DefaultSettings, get_settings
from .endpoints import list_of_routes
from .utils.common import get_hostname
from .utils.logging import logging_middleware


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def connect_middlewares(application: FastAPI) -> None:
    application.middleware("http")(logging_middleware)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Api ebana rot za dva dna"

    tags_metadata = [
        {
            "name": "Application Health",
            "description": "API health check.",
        },
    ]

    application = FastAPI(
        title="Api cyka",
        description=description,
        docs_url="/api/swagger",
        openapi_url="/api/openapi",
        version="0.1.0",
        openapi_tags=tags_metadata,
    )
    settings = get_settings()
    bind_routes(application, settings)
    add_pagination(application)
    connect_middlewares(application)
    application.state.settings = settings
    return application


app = get_app()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    settings_for_application = get_settings()
    run(
        "app.__main__:app",
        host=get_hostname(settings_for_application.APP_HOST),
        port=settings_for_application.APP_PORT,
        reload=True,
        reload_dirs=["app"],
        log_level="debug",
    )
