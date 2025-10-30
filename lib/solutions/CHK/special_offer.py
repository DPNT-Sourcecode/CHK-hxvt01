from abc import ABC


class SpecialOffer(ABC):
    def __init__(self, item: str, count_of_items: int) -> None:
        self.item = item
        self.num_items_to_qualify = count_of_items


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
