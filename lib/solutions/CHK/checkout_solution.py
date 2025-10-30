from collections import Counter

_item_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

_items = _item_prices.keys()


class SpecialOffer:
    def __init__(self, count_of_items: int, price: int) -> None:
        self.count_of_items = count_of_items
        self.price = price


_special_offers = {
    "A": SpecialOffer(count_of_items=3, price=130),
    "B": SpecialOffer(count_of_items=2, price=45),
}


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self._skus_valid(skus):
            return -1

        item_counts = Counter(skus)
        total = 0
        for item, count in item_counts.items():
            if item in _special_offers:
                if count >= _special_offers[item].count_of_items:
                    num_special_offers, remainder = divmod(
                        count, _special_offers[item].count_of_items
                    )
                    total += _special_offers[item].price * num_special_offers
                    item_counts[item] = remainder

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





