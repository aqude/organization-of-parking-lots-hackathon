FROM python:3.11 as requirements-stage

WORKDIR /fastapi_app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /fastapi_app/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /code

COPY --from=requirements-stage /fastapi_app/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./wait-for /code/wait-for
COPY ./docker_scripts /code/docker_scripts

RUN chmod a+x /code/docker_scripts/*.sh


