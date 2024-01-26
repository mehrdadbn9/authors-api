ARG PYTHON_VERSION=3.9-slim-bullseye

FROM python:${PYTHON_VERSION} as python

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

## --no-install-recommends
RUN apt-get update && apt-get install --no-install-recommends -y \
   build-essential \
   libpq-dev 

COPY ./requirements .

# whee
RUN pip wheel --wheel-dir /usr/src/app/wheels \
   -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

# prevent using bytecode .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# disable buffer and using disk
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# prevent removing important package by --auto-remove -o APT::AutoRemove::RecommendsImportant=false 
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
# make it usable in windows like linux ,...
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]