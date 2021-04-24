"""Factory for the API."""
import logging.config

from fastapi import FastAPI

from api import configuration


def create_api():
    """Create the API."""
    config = configuration.from_envvar()
    app = FastAPI(
        title=config["API_NAME"],
        version=config["VERSION"],
        openapi_url=f'{config["API_PREFIX"]}/{config["OPENAPI_URL"]}',
        docs_url=f'{config["API_PREFIX"]}/{config["DOCS_URL"]}',
        redoc_url=f'{config["API_PREFIX"]}/{config["REDOC_URL"]}',
    )
    app.config = config

    setup_logger(app, log_name="api")
    setup_routes(app)

    return app


def setup_logger(app, log_name=None):
    """Set up the logger."""
    logging.config.fileConfig("logging.conf")
    app.logger = logging.getLogger(log_name if log_name else app.config["API_NAME"])
    app.logger.info("config", extra={"config": app.config})


def setup_routes(app):
    """Register routes."""
    from api.routers import basic, humanize

    app.include_router(basic.router, prefix=app.config["API_PREFIX"])
    app.include_router(humanize.router, prefix=app.config["API_PREFIX"])
