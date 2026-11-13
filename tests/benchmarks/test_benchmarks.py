"""Performance benchmarks; run with `make benchmark`, never with the unit tests."""

from nutria import hello


def test_hello_benchmark(benchmark) -> None:
    result = benchmark(hello)
    assert result
