FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /tmp/
RUN poetry export --format requirements.txt --output requirements.txt --without-hashes

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /api

RUN pip install poetry

COPY --from=requirements-stage /tmp/requirements.txt ./requirements.txt
RUN pip install --no-cache --upgrade pip==22.2 \
    && pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

ENV KIND 'api'

CMD ["uvicorn", "--host=0.0.0.0", "--port=8080", "--log-level", "debug", "src.delivery.web.run:app", "--reload"]
