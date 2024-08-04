.PHONY: benchmark
benchmark:
	richbench --percentage --repeat 3 benchmarks/

.PHONY: test
test:
	pytest tests/
