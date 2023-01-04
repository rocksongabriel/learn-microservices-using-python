FROM python:3.11-alpine

# setup the environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDEFAULTHANDLER 1

# install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc


WORKDIR /app

# install dependencies
COPY ../Pipfile /app/
COPY ../Pipfile.lock /app/
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# Install application into container
COPY . .