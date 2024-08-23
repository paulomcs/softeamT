SHELL:=/bin/bash
ROOT:=../..

test:
	source $(ROOT)/.venv/bin/activate && pytest $(ROOT)

setup: pyenv

pyenv: build-pyenv requirements test_requirements

build-pyenv:
	python3 -m venv $(ROOT)/.venv

requirements:
	source $(ROOT)/.venv/bin/activate && pip3 install -r $(ROOT)/requirements.txt

test_requirements:
	source $(ROOT)/.venv/bin/activate && pip3 install -r $(ROOT)/test_requirements.txt
