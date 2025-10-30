from collections import Counter

from lib.solutions.CHK.item_price_catalogue import ITEM_PRICES, UNIQUE_ITEMS
from lib.solutions.CHK.special_offer import (
    PRIORITISED_SPECIAL_OFFERS,
    MultiBuyOffer,
    BuyAndGetFreeOffer,
)


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str) -> int:
        if not self._skus_valid(skus):
            return -1

        shopping_list = Counter(skus)
        total, remaining_shopping_list = self._calculate_special_offers(shopping_list)

        for item, count in remaining_shopping_list.items():
            item_price = ITEM_PRICES[item]
            total += item_price * count

        return total

    def _skus_valid(self, skus: str) -> bool:
        for sku in skus:
            if sku not in UNIQUE_ITEMS:
                return False
        return True

    def _calculate_special_offers(self, shopping_list: dict) -> tuple[int, dict]:
        remaining_shop_list = shopping_list.copy()
        total = 0
        for offer in PRIORITISED_SPECIAL_OFFERS:
            if offer.item in remaining_shop_list:
                item, item_count = offer.item, remaining_shop_list[offer.item]

                num_special_offers, remainder = divmod(
                    item_count, offer.num_items_to_qualify
                )
                if isinstance(offer, MultiBuyOffer):
                    total += offer.price * num_special_offers
                elif isinstance(offer, BuyAndGetFreeOffer):
                    remaining_shop_list[offer.free_item] = max(
                        0,
                        remaining_shop_list[offer.free_item] - (1 * num_special_offers),
                    )

                    total += ITEM_PRICES[item] * (remaining_shop_list[item] - remainder)
                else:
                    raise NotImplementedError(
                        f"Offertype {type(offer)} is not implemented."
                    )
                remaining_shop_list[item] = remainder

        return total, remaining_shop_list


