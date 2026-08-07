.PHONY: help install test lint format clean

help:
	@echo "CivicLens AI development commands"
	@echo ""
	@echo "make install   Install development dependencies"
	@echo "make test      Run tests"
	@echo "make lint      Run code checks"
	@echo "make format    Format Python code"
	@echo "make clean     Remove temporary files"

install:
	python -m pip install --upgrade pip
	python -m pip install -e .

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov
