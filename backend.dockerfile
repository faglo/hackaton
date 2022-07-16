FROM python:3.8-slim AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y gcc

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.8-slim AS build-image
COPY --from=compile-image /opt/venv /opt/venv
WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"
RUN chmod +x ./upgrade_migrations.sh

ENTRYPOINT ["./upgrade_migrations.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload", "--debug"]
