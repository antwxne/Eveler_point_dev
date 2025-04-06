FROM python:3.11.7

RUN pip install uv

WORKDIR /app

COPY ./pyproject.toml ./pyproject.toml
COPY .python-version .python-version

RUN uv sync

COPY app .

CMD ["uv", "run", "fastapi", "run"]