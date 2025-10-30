from solutions.HLO.sum_solution import HelloSolution


class TestSum:
    def test_sum(self) -> None:
        assert HelloSolution().hello("Harry") == "Hello, Harry!"
