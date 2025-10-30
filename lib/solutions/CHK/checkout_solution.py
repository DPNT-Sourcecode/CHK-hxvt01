from collections import Counter

_item_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

_items = _item_prices.keys()


class SpecialOffer:
    def __init__(self, count_of_items: int, special_price: int) -> None:
        self.count_of_items = count_of_items
        self.special_price = special_price


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self._skus_valid(skus):
            return -1

        item_counts = Counter(skus)
        total = 0
        for item, count in item_counts.items():
            ...

        # Calculate remainders
        for item, count in item_counts.items():
            item_price = _item_prices[item]
            total += item_price * count

        return total

    def _skus_valid(self, skus: str) -> bool:
        for sku in skus:
            if sku not in _items:
                return False
        return True



