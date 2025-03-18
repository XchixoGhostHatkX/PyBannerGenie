# Makefile for PyBannerGenie

.PHONY: install format lint test clean

install:
	python3 -m venv venv
	source venv/bin/activate  # On Linux/macOS
	venv\Scripts\activate  # On Windows
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black src tests

lint:
	flake8 src tests

test:
	python -m unittest discover -s tests

clean:
	rm -rf venv
	find . -name "__pycache__" -exec rm -rf {} \;
	find . -name "*.pyc" -exec rm -f {} \;

run:
	python src/PyBannerGenie.py
