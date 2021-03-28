all: lint format

lint: mypy
check: lint

mypy:
	mypy --pretty --show-error-codes backgrounder/

format:
	./script/format

.PHONY: mypy lint format check all
