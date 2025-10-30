import pytest
from solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_hello(self) -> None:
        assert HelloSolution().hello("Harry") == "Hello, Harry!"

    def test_raise_error_when_name_none(self) -> None:
        with pytest.raises(ValueError):
            HelloSolution().hello(None)

    def test_raise_error_when_name_longer_than_100_chars(self) -> None:
        name = "a" * 101

        with pytest.raises(ValueError):
            HelloSolution().hello(name)


