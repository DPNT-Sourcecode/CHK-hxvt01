from abc import ABC
from collections import Counter

_item_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

_items = _item_prices.keys()


class SpecialOffer(ABC):
    def __init__(self, item: str, count_of_items: int) -> None:
        self.item = item
        self.count_of_items = count_of_items


class MultiOffer(SpecialOffer):
    def __init__(self, item: str, count_of_items: int, price: int) -> None:
        super().__init__(item, count_of_items)
        self.price = price


class GetFreeOffer(SpecialOffer):
    def __init__(self, item: str, count_of_items: int, free_item: str) -> None:
        super().__init__(item, count_of_items)
        self.free_item = free_item


_prioritised_special_offers = [
    MultiOffer(item="A", count_of_items=5, price=200),
    MultiOffer(item="A", count_of_items=3, price=130),
    GetFreeOffer(item="E", count_of_items=2, free_item="B"),
    MultiOffer(item="B", count_of_items=2, price=45),
]


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self._skus_valid(skus):
            return -1

        shopping_list = Counter(skus)
        total, remaining_shopping_list = self._calculate_special_offers(shopping_list)

        for item, count in remaining_shopping_list.items():
            item_price = _item_prices[item]
            total += item_price * count

        return total

    def _skus_valid(self, skus: str) -> bool:
        for sku in skus:
            if sku not in _items:
                return False
        return True

    def _calculate_special_offers(self, shopping_list: dict) -> tuple[int, dict]:
        remaining_shopping_list = shopping_list.copy()
        total = 0
        for offer in _prioritised_special_offers:
            if offer.item in remaining_shopping_list:
                item, count = offer.item, remaining_shopping_list[offer.item]

                if count >= offer.count_of_items:
                    if isinstance(offer, MultiOffer):
                        num_special_offers, remainder = divmod(
                            count, offer.count_of_items
                        )
                        total += offer.price * num_special_offers
                        remaining_shopping_list[item] = remainder
                    elif isinstance(offer, GetFreeOffer):
                        remainder_after_given_for_free = max(
                            0, remaining_shopping_list[offer.free_item] - 1
                        )
                        remaining_shopping_list[offer.free_item] -= (
                            remainder_after_given_for_free
                        )
                        total += offer.count_of_items * _item_prices[offer.item]
                        remaining_shopping_list[offer.item] -= offer.count_of_items
                    else:
                        raise NotImplementedError(
                            f"Offertype {type(offer)} is not implemented."
                        )

        return total, remaining_shopping_list

