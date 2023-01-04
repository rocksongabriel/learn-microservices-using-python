FROM python:3.11-slim-buster

# setup the environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDEFAULTHANDLER 1
ENV PYTHONUNBUFFER 1

WORKDIR /app

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Install application into container
COPY . /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]