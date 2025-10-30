from collections import Counter

_item_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

_items = _item_prices.keys()


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        for sku in skus:
            if sku not in _items:
                return -1

        item_counts = Counter(skus)

        total = 0
        for item, count in item_counts.items():
            item_price = _item_prices[item]
            total += item_price * count

        return total


