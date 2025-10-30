
_item_prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        item_counts = Counter(skus)

        raise NotImplementedError()

