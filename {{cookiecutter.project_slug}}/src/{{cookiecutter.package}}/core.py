"""Provide the core FastAPI application."""
from fastapi import FastAPI

from {{cookiecutter.package}} import __version__


if 'untagged' in __version__ or 'unknown':
    API_VERSION = 0
else:
    API_VERSION = __version__.split('.')[0]


app = FastAPI(title='{{cookiecutter.package}}',
              description='{{cookiecutter.description}}',
              version=__version__,
              openapi_url=f"/api/v{API_VERSION}/openapi.json",
              docs_url='/api/docs',
              redoc_url='/api/redoc')
