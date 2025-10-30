from solutions.HLO.hello_solution import HelloSolution


class TestHello:
    def test_hello(self) -> None:
        assert HelloSolution().hello("Craftsman") == "Hello, Craftsman!"

    def test_hello_mr_x(self) -> None:
        assert HelloSolution().hello("Mr. X") == "Hello, Mr. X!"
