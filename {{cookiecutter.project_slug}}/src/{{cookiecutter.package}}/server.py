"""Run the fastapi app in a server."""
import uvicorn

from {{cookiecutter.package}}.core import app


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', debug=True, port=8001)
