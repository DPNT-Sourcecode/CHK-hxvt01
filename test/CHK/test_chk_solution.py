from solutions.CHK.hello_solution import CheckoutSolution


class TestCheckout:
    def test_checkout_one_of_each_order_does_not_matter(self) -> None:
        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DCBA") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DBCA") == 50 + 30 + 20 + 15

    def test_checkout_special_offers_order_does_not_matter(self) -> None:
        assert CheckoutSolution().checkout("AAABB") == 130 + 45
        assert CheckoutSolution().checkout("ABABA") == 130 + 45
        assert CheckoutSolution().checkout("BBAAA") == 130 + 45

    def test_checkout_multiple_special_offers_with_remainder(self) -> None:
        assert CheckoutSolution().checkout("AAAAAAAA") == 130 + 130 + 100
        assert CheckoutSolution().checkout("BBBBBBB") == 45 + 45 + 45 + 30

    def test_checkout_complex_order(self) -> None:
        assert CheckoutSolution().checkout("AAAAABBCCCDDD") == 130 + 100 + 45 + 60 + 45

