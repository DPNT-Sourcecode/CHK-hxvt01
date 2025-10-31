from collections import Counter

from solutions.CHK.item_price_catalogue import ITEM_PRICES
from solutions.CHK.special_offer import (
    PRIORITISED_SPECIAL_OFFERS,
    MultiBuyOffer,
    BuyAndGetFreeOffer,
)
from solutions.CHK.item_price_catalogue import ItemPriceCatalogue


class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus: str, item_prices: ItemPriceCatalogue | None = None) -> int:
        if item_prices is None:
            item_prices = ITEM_PRICES

        if not self._skus_valid(skus, item_prices):
            return -1

        shopping_list = Counter(skus)
        total, remaining_shopping_list = self._calculate_special_offers(shopping_list)

        for item, count in remaining_shopping_list.items():
            item_price = item_prices[item]
            total += item_price * count

        return total

    def _skus_valid(self, skus: str, item_prices: ItemPriceCatalogue) -> bool:
        for sku in skus:
            if sku not in item_prices.keys():
                return False
        return True

    def _calculate_special_offers(
        self, shopping_list: dict, item_prices: ItemPriceCatalogue
    ) -> tuple[int, dict]:
        remain_shop_list = shopping_list.copy()
        total = 0
        for offer in PRIORITISED_SPECIAL_OFFERS:
            if offer.item in remain_shop_list:
                item, item_count = offer.item, remain_shop_list[offer.item]

                num_times_apply_offer, remainder = divmod(
                    item_count, offer.num_items_to_qualify
                )
                if num_times_apply_offer:
                    print(
                        f"Applying special offer {num_times_apply_offer} times: {offer}"
                    )

                if isinstance(offer, MultiBuyOffer):
                    total += offer.price * num_times_apply_offer
                elif isinstance(offer, BuyAndGetFreeOffer):
                    num_free_items = 1 * num_times_apply_offer
                    remain_shop_list[offer.free_item] = max(
                        0,
                        remain_shop_list[offer.free_item] - num_free_items,
                    )

                    total += item_prices[item] * (remain_shop_list[item] - remainder)
                else:
                    raise NotImplementedError(
                        f"Offertype {type(offer)} is not implemented."
                    )
                remain_shop_list[item] = remainder

        return total, remain_shop_list



