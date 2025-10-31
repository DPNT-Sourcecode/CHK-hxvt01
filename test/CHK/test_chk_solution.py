import pytest
from solutions.CHK.checkout_solution import CheckoutSolution

from lib.solutions.CHK.item_price_catalogue import ItemPriceCatalogue


class TestCheckout:
    def test_checkout_one_of_each_order_does_not_matter(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert (
            CheckoutSolution().checkout("ABCDL", item_price_catalogue)
            == 50 + 30 + 20 + 15 + 90
        )
        assert (
            CheckoutSolution().checkout("LDCBA", item_price_catalogue)
            == 50 + 30 + 20 + 15 + 90
        )
        assert (
            CheckoutSolution().checkout("LDBCA", item_price_catalogue)
            == 50 + 30 + 20 + 15 + 90
        )

    def test_checkout_special_offers_order_does_not_matter(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert CheckoutSolution().checkout("AAABB", item_price_catalogue) == 130 + 45
        assert CheckoutSolution().checkout("ABABA", item_price_catalogue) == 130 + 45
        assert CheckoutSolution().checkout("BBAAA", item_price_catalogue) == 130 + 45

    def test_checkout_multiple_special_offers_with_remainder(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert (
            CheckoutSolution().checkout("AAAAAAAA", item_price_catalogue) == 200 + 130
        )
        assert (
            CheckoutSolution().checkout("BBBBBBB", item_price_catalogue)
            == 45 + 45 + 45 + 30
        )

    def test_checkout_complex_shopping_list(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert (
            CheckoutSolution().checkout(
                "AAAAABBCCCDDDEEEFFFVVVRRRQRRR",
                item_price_catalogue,
            )
            == 200 + 30 + 60 + 45 + 120 + 20 + 130 + 150 + 150
        )
        assert (
            CheckoutSolution().checkout(
                "ARARAVFCRBVBQCCRDVFRADEREFDEA",
                item_price_catalogue,
            )
            == 200 + 30 + 60 + 45 + 120 + 20 + 130 + 150 + 150
        )

    def test_return_minus_one_on_illegal_input(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert CheckoutSolution().checkout("AAB2", item_price_catalogue) == -1
        assert CheckoutSolution().checkout("123", item_price_catalogue) == -1
        assert CheckoutSolution().checkout("!@#", item_price_catalogue) == -1

    def test_buy_get_free_offer_when_free_item_not_present(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert CheckoutSolution().checkout("EE", item_price_catalogue) == 80
        assert CheckoutSolution().checkout("EEEE", item_price_catalogue) == 160

    def test_checkout_favor_customer_when_applying_offers(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert (
            CheckoutSolution().checkout("AAAAAA", item_price_catalogue) == 200 + 50
        )  # favour 5A for 200
        assert (
            CheckoutSolution().checkout("BBEE", item_price_catalogue) == 80 + 30
        )  # favour 1 B for free
        assert (
            CheckoutSolution().checkout("BBBBEEE", item_price_catalogue) == 75 + 120
        )  # favor buy get B free

    def test_checkout_buy_multiple_of_item_get_another_free(
        self, item_price_catalogue: ItemPriceCatalogue
    ) -> None:
        assert CheckoutSolution().checkout("FFF", item_price_catalogue) == 20
        assert CheckoutSolution().checkout("FF", item_price_catalogue) == 20
        assert CheckoutSolution().checkout("FFFFF", item_price_catalogue) == 40
        assert CheckoutSolution().checkout("FFFFFF", item_price_catalogue) == 40
        assert CheckoutSolution().checkout("UUUU", item_price_catalogue) == 120
        assert CheckoutSolution().checkout("UFUFUFU", item_price_catalogue) == 140


@pytest.fixture
def item_price_catalogue() -> ItemPriceCatalogue:
    return {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }


