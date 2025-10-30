from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout:
    def test_checkout_one_of_each_order_does_not_matter(self) -> None:
        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DCBA") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DBCA") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("EE") == 80

    def test_checkout_special_offers_order_does_not_matter(self) -> None:
        assert CheckoutSolution().checkout("AAABB") == 130 + 45
        assert CheckoutSolution().checkout("ABABA") == 130 + 45
        assert CheckoutSolution().checkout("BBAAA") == 130 + 45

    def test_checkout_multiple_special_offers_with_remainder(self) -> None:
        assert CheckoutSolution().checkout("AAAAAAAA") == 200 + 130
        assert CheckoutSolution().checkout("BBBBBBB") == 45 + 45 + 45 + 30

    def test_checkout_complex_order(self) -> None:
        assert CheckoutSolution().checkout("AAAAABBCCCDDD") == 200 + 45 + 60 + 45

    def test_return_minus_one_on_illegal_input(self) -> None:
        assert CheckoutSolution().checkout("AABX") == -1
        assert CheckoutSolution().checkout("123") == -1
        assert CheckoutSolution().checkout("!@#") == -1

    def test_checkout_favor_customer_when_applying_offers(self) -> None:
        # assert CheckoutSolution().checkout("AAAAAA") == 200 + 50  # favour 5A for 200
        # assert CheckoutSolution().checkout("BBEE") == 80 + 30  # favour 1 B for free
        assert CheckoutSolution().checkout("BBBBEEE") == 75 + 120
