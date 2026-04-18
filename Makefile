install:
	poetry install --only=ci --no-root 

install-dev:
	poetry install --only=dev --no-root

load:
	poetry run python src/main.py --path /workspaces/ml_practice/data/raw/credit_score.csv

lint:
	poetry run ruff check src tests

format:
	poetry run ruff check --fix src tests

test:
	poetry run pytest

check: format lint test