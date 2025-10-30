from solutions.CHK.hello_solution import CheckoutSolution


class TestCheckout:
    def test_checkout(self) -> None:
        assert CheckoutSolution().foo() is None
