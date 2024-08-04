.PHONY: benchmark
benchmark:
	poetry run richbench --profile --percentage --markdown --repeat 10 ./

.PHONY: test
test:
	pytest tests/
