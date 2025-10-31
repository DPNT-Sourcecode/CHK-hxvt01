from abc import ABC


class SpecialOffer(ABC):
    pass


class MultiBuyOffer(SpecialOffer):
    def __init__(self, item: str, num_items_to_qualify: int, price: int) -> None:
        self.item = item
        self.num_items_to_qualify = num_items_to_qualify
        self.price = price

    def __str__(self) -> str:
        return f"{self.num_items_to_qualify}{self.item} for {self.price}"


class BuyAndGetFreeOffer(SpecialOffer):
    def __init__(self, item: str, num_items_to_qualify: int, free_item: str) -> None:
        self.item = item
        self.num_items_to_qualify = num_items_to_qualify
        self.free_item = free_item

    def __str__(self) -> str:
        return f"{self.num_items_to_qualify}{self.item} get one {self.free_item} free"


class GroupDiscountOffer(SpecialOffer):
    def __init__(self, items: list[str], num_items_to_qualify: int, price: int) -> None:
        self.items = items
        self.num_items_to_qualify = num_items_to_qualify
        self.price = price

    def __str__(self) -> str:
        return f"buy any {self.num_items_to_qualify} of {list(self.items)} for {self.price}"


PRIORITISED_SPECIAL_OFFERS = [
    MultiBuyOffer(item="A", num_items_to_qualify=5, price=200),
    MultiBuyOffer(item="A", num_items_to_qualify=3, price=130),
    BuyAndGetFreeOffer(item="E", num_items_to_qualify=2, free_item="B"),
    MultiBuyOffer(item="B", num_items_to_qualify=2, price=45),
    MultiBuyOffer(item="F", num_items_to_qualify=3, price=20),
    MultiBuyOffer(item="H", num_items_to_qualify=10, price=80),
    MultiBuyOffer(item="H", num_items_to_qualify=5, price=45),
    MultiBuyOffer(item="K", num_items_to_qualify=2, price=120),
    BuyAndGetFreeOffer(item="N", num_items_to_qualify=3, free_item="M"),
    MultiBuyOffer(item="P", num_items_to_qualify=5, price=200),
    BuyAndGetFreeOffer(item="R", num_items_to_qualify=3, free_item="Q"),
    MultiBuyOffer(item="Q", num_items_to_qualify=3, price=80),
    MultiBuyOffer(item="U", num_items_to_qualify=4, price=120),
    MultiBuyOffer(item="V", num_items_to_qualify=3, price=130),
    MultiBuyOffer(item="V", num_items_to_qualify=2, price=90),
]

