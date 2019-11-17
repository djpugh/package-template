FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# COPY docker/prestart.sh /app/prestart.sh

ENV APP_MODULE={{cookiecutter.package}}.core:app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

CMD ["/start.sh"]

COPY docker-build /dist
RUN pip install /dist/$(ls -t /dist | head -n1) # pip install the latest created file in dist folder. this should be the wheel file.
