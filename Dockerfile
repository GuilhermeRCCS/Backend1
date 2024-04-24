FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY . .

EXPOSE 8000

RUN poetry install

ENTRYPOINT ["poetry","run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]