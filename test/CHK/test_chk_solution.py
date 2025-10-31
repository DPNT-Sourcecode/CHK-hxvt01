import pytest
from solutions.CHK.checkout_solution import CheckoutSolution
from solutions.CHK.item_price_catalogue import ItemPriceCatalogue

from solutions.CHK.special_offer import (
    SpecialOffer,
    MultiBuyOffer,
    BuyAndGetFreeOffer,
)


class TestCheckout:
    def test_checkout_one_of_each_order_does_not_matter(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert (
            CheckoutSolution().checkout("ABCDL", item_prices, special_offers)
            == 50 + 30 + 20 + 15 + 90
        )
        assert (
            CheckoutSolution().checkout("LDCBA", item_prices, special_offers)
            == 50 + 30 + 20 + 15 + 90
        )
        assert (
            CheckoutSolution().checkout("LDBCA", item_prices, special_offers)
            == 50 + 30 + 20 + 15 + 90
        )

    def test_checkout_special_offers_order_does_not_matter(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert (
            CheckoutSolution().checkout("AAABB", item_prices, special_offers)
            == 130 + 45
        )
        assert (
            CheckoutSolution().checkout("ABABA", item_prices, special_offers)
            == 130 + 45
        )
        assert (
            CheckoutSolution().checkout("BBAAA", item_prices, special_offers)
            == 130 + 45
        )

    def test_checkout_multiple_special_offers_with_remainder(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert (
            CheckoutSolution().checkout("AAAAAAAA", item_prices, special_offers)
            == 200 + 130
        )
        assert (
            CheckoutSolution().checkout("BBBBBBB", item_prices, special_offers)
            == 45 + 45 + 45 + 30
        )

    def test_checkout_complex_shopping_list(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert (
            CheckoutSolution().checkout(
                "AAAAABBCCCDDDEEEFFFVVVRRRQRRR", item_prices, special_offers
            )
            == 200 + 30 + 60 + 45 + 120 + 20 + 130 + 150 + 150
        )
        assert (
            CheckoutSolution().checkout(
                "ARARAVFCRBVBQCCRDVFRADEREFDEA", item_prices, special_offers
            )
            == 200 + 30 + 60 + 45 + 120 + 20 + 130 + 150 + 150
        )

    def test_return_minus_one_on_illegal_input(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert CheckoutSolution().checkout("AAB2", item_prices, special_offers) == -1
        assert CheckoutSolution().checkout("123", item_prices, special_offers) == -1
        assert CheckoutSolution().checkout("!@#", item_prices, special_offers) == -1

    def test_buy_get_free_offer_when_free_item_not_present(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert CheckoutSolution().checkout("EE", item_prices, special_offers) == 80
        assert CheckoutSolution().checkout("EEEE", item_prices, special_offers) == 160

    def test_checkout_favor_customer_when_applying_offers(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert (
            CheckoutSolution().checkout("AAAAAA", item_prices, special_offers)
            == 200 + 50
        )  # favour 5A for 200
        assert (
            CheckoutSolution().checkout("BBEE", item_prices, special_offers) == 80 + 30
        )  # favour 1 B for free
        assert (
            CheckoutSolution().checkout("BBBBEEE", item_prices, special_offers)
            == 75 + 120
        )  # favor buy get B free

    def test_checkout_buy_multiple_of_item_get_another_free(
        self, item_prices: ItemPriceCatalogue, special_offers: list[SpecialOffer]
    ) -> None:
        assert CheckoutSolution().checkout("FFF", item_prices, special_offers) == 20
        assert CheckoutSolution().checkout("FF", item_prices, special_offers) == 20
        assert CheckoutSolution().checkout("FFFFF", item_prices, special_offers) == 40
        assert CheckoutSolution().checkout("FFFFFF", item_prices, special_offers) == 40
        assert CheckoutSolution().checkout("UUUU", item_prices, special_offers) == 120
        assert (
            CheckoutSolution().checkout("UFUFUFU", item_prices, special_offers) == 140
        )


@pytest.fixture
def item_prices() -> ItemPriceCatalogue:
    return {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "L": 90,
        "M": 15,
        "N": 40,
        "Q": 30,
        "R": 50,
        "U": 40,
        "V": 50,
    }


@pytest.fixture
def special_offers() -> list[SpecialOffer]:
    return [
        MultiBuyOffer(item="A", num_items_to_qualify=5, price=200),
        MultiBuyOffer(item="A", num_items_to_qualify=3, price=130),
        BuyAndGetFreeOffer(item="E", num_items_to_qualify=2, free_item="B"),
        MultiBuyOffer(item="B", num_items_to_qualify=2, price=45),
        MultiBuyOffer(item="F", num_items_to_qualify=3, price=20),
        MultiBuyOffer(item="H", num_items_to_qualify=10, price=80),
        MultiBuyOffer(item="H", num_items_to_qualify=5, price=45),
        MultiBuyOffer(item="K", num_items_to_qualify=2, price=150),
        BuyAndGetFreeOffer(item="N", num_items_to_qualify=3, free_item="M"),
        MultiBuyOffer(item="P", num_items_to_qualify=5, price=200),
        BuyAndGetFreeOffer(item="R", num_items_to_qualify=3, free_item="Q"),
        MultiBuyOffer(item="Q", num_items_to_qualify=3, price=80),
        MultiBuyOffer(item="U", num_items_to_qualify=4, price=120),
        MultiBuyOffer(item="V", num_items_to_qualify=3, price=130),
        MultiBuyOffer(item="V", num_items_to_qualify=2, price=90),
    ]






