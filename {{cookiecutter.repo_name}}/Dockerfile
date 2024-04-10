ARG BASE_IMAGE=python:3.8.16-slim-buster
FROM $BASE_IMAGE

ENV POETRY_HOME=/etc/poetry \
    POETRY_VERSION=1.4.2 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_NO_INTERACTION=1

RUN BUILD_DEPS='curl' \
    && apt-get update -y \
    && apt-get install --no-install-recommends -y \
        $BUILD_DEPS \
    && apt-get install --no-install-recommends -y openssh-client \
    && rm -r /var/lib/apt/lists/* \
    # Install poetry
    && curl -sSL https://install.python-poetry.org | python \
    && apt-get purge -y --auto-remove $BUILD_DEPS

# add github.com to known hosts
RUN mkdir -p -m 0600 ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts

WORKDIR /code
COPY ./{{cookiecutter.repo_name}} ./{{cookiecutter.repo_name}}
COPY ./tests ./tests

# install project requirements
COPY ./pyproject.toml ./
RUN --mount=type=ssh $POETRY_HOME/bin/poetry lock && $POETRY_HOME/bin/poetry install --no-root
