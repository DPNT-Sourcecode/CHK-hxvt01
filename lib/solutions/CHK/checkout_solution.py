from abc import ABC
from collections import Counter

_ITEM_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
}

_UNIQUE_ITEMS = _ITEM_PRICES.keys()


class SpecialOffer(ABC):
    def __init__(self, item: str, count_of_items: int) -> None:
        self.item = item
        self.num_of_items_to_qualify = count_of_items


class MultiOffer(SpecialOffer):
    def __init__(self, item: str, count_of_items: int, price: int) -> None:
        super().__init__(item, count_of_items)
        self.price = price


class GetFreeOffer(SpecialOffer):
    def __init__(self, item: str, count_of_items: int, free_item: str) -> None:
        super().__init__(item, count_of_items)
        self.free_item = free_item


_PRIORITISED_SPECIAL_OFFERS = [
    MultiOffer(item="A", count_of_items=5, price=200),
    MultiOffer(item="A", count_of_items=3, price=130),
    GetFreeOffer(item="E", count_of_items=2, free_item="B"),
    MultiOffer(item="B", count_of_items=2, price=45),
    MultiOffer(item="F", count_of_items=3, price=20),
]


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self._skus_valid(skus):
            return -1

        shopping_list = Counter(skus)
        total, remaining_shopping_list = self._calculate_special_offers(shopping_list)

        for item, count in remaining_shopping_list.items():
            item_price = _ITEM_PRICES[item]
            total += item_price * count

        return total

    def _skus_valid(self, skus: str) -> bool:
        for sku in skus:
            if sku not in _UNIQUE_ITEMS:
                return False
        return True

    def _calculate_special_offers(self, shopping_list: dict) -> tuple[int, dict]:
        remaining_shopping_list = shopping_list.copy()
        total = 0
        for offer in _PRIORITISED_SPECIAL_OFFERS:
            if offer.item in remaining_shopping_list:
                item, item_count = offer.item, remaining_shopping_list[offer.item]

                if item_count >= offer.num_of_items_to_qualify:
                    num_special_offers, remainder = divmod(
                        item_count, offer.num_of_items_to_qualify
                    )
                    if isinstance(offer, MultiOffer):
                        total += offer.price * num_special_offers
                    elif isinstance(offer, GetFreeOffer):
                        remaining_shopping_list[offer.free_item] = max(
                            0,
                            remaining_shopping_list[offer.free_item]
                            - (1 * num_special_offers),
                        )

                        total += _ITEM_PRICES[item] * (
                            remaining_shopping_list[item] - remainder
                        )
                    else:
                        raise NotImplementedError(
                            f"Offertype {type(offer)} is not implemented."
                        )
                    remaining_shopping_list[item] = remainder

        return total, remaining_shopping_list






