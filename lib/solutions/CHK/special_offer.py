from abc import ABC


class SpecialOffer(ABC):
    def __init__(self, item: str, count_of_items: int) -> None:
        self.item = item
        self.num_items_to_qualify = count_of_items


class MultiBuyOffer(SpecialOffer):
    def __init__(self, item: str, count_of_items: int, price: int) -> None:
        super().__init__(item, count_of_items)
        self.price = price


class BuyAndGetFreeOffer(SpecialOffer):
    def __init__(self, item: str, count_of_items: int, free_item: str) -> None:
        super().__init__(item, count_of_items)
        self.free_item = free_item


PRIORITISED_SPECIAL_OFFERS = [
    MultiBuyOffer(item="A", count_of_items=5, price=200),
    MultiBuyOffer(item="A", count_of_items=3, price=130),
    BuyAndGetFreeOffer(item="E", count_of_items=2, free_item="B"),
    MultiBuyOffer(item="B", count_of_items=2, price=45),
    MultiBuyOffer(item="F", count_of_items=3, price=20),
]

