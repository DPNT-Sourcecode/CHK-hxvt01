from collections import Counter

from solutions.CHK.item_price_catalogue import ITEM_PRICES
from solutions.CHK.special_offer import (
    PRIORITISED_SPECIAL_OFFERS,
    MultiBuyOffer,
    BuyAndGetFreeOffer,
)
from solutions.CHK.item_price_catalogue import ItemPriceCatalogue

from solutions.CHK.special_offer import SpecialOffer

from solutions.CHK.special_offer import GroupDiscountOffer


class CheckoutSolution:
    # skus = unicode string
    def checkout(
        self,
        skus: str,
        item_prices: ItemPriceCatalogue | None = None,
        special_offers: list[SpecialOffer] | None = None,
    ) -> int:
        if item_prices is None:
            item_prices = ITEM_PRICES
        if special_offers is None:
            special_offers = PRIORITISED_SPECIAL_OFFERS

        if not self._skus_valid(skus, item_prices):
            return -1

        shopping_list = Counter(skus)
        total, remaining_shopping_list = self._calculate_special_offers(
            shopping_list, item_prices, special_offers
        )

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
        self,
        shopping_list: dict,
        item_prices: ItemPriceCatalogue,
        special_offers: list[SpecialOffer],
    ) -> tuple[int, dict]:
        remain_shop_list = shopping_list.copy()
        total = 0
        for offer in special_offers:
            match offer:
                case MultiBuyOffer():
                    total += self._apply_multi_buy_offer(remain_shop_list, offer)
                case BuyAndGetFreeOffer():
                    total += self._apply_buy_and_get_free_offer(
                        item_prices, offer, remain_shop_list
                    )
                case GroupDiscountOffer():
                    total += self._apply_group_discount_offer(offer, remain_shop_list)
                case _:
                    raise NotImplementedError(
                        f"Offertype {type(offer)} is not implemented."
                    )

        return total, remain_shop_list

    def _apply_buy_and_get_free_offer(
        self,
        item_prices: ItemPriceCatalogue,
        offer: BuyAndGetFreeOffer,
        shop_list: dict[str, int],
    ) -> int:
        total = 0
        if offer.item in shop_list:
            item, item_count = offer.item, shop_list[offer.item]

            num_times_apply_offer, remainder = divmod(
                item_count, offer.num_items_to_qualify
            )
            if num_times_apply_offer:
                print(f"Applying special offer {num_times_apply_offer} times: {offer}")
            num_free_items = 1 * num_times_apply_offer
            shop_list[offer.free_item] = max(
                0,
                shop_list[offer.free_item] - num_free_items,
            )

            total += item_prices[item] * (shop_list[item] - remainder)
            shop_list[item] = remainder
        return total

    def _apply_multi_buy_offer(
        self, shopping_list: dict[str, int], offer: MultiBuyOffer
    ) -> int:
        total = 0
        if offer.item in shopping_list:
            item, item_count = offer.item, shopping_list[offer.item]

            num_times_apply_offer, remainder = divmod(
                item_count, offer.num_items_to_qualify
            )
            if num_times_apply_offer:
                print(f"Applying special offer {num_times_apply_offer} times: {offer}")
            shopping_list[item] = remainder
            total += offer.price * num_times_apply_offer
        return total

    def _apply_group_discount_offer(
        self, offer: GroupDiscountOffer, shopping_list: dict[str, int]
    ) -> int:
        total = 0
        while shopping_list != {}:
            num_items_to_qualify = offer.num_items_to_qualify
            disc_group = {}

            for item in offer.items:
                if item in shopping_list:
                    num_items_to_include = min(
                        num_items_to_qualify, shopping_list[item]
                    )
                    disc_group[item] = num_items_to_include
                    num_items_to_qualify -= num_items_to_include

                    if num_items_to_qualify == 0:
                        print(
                            f"Applying special offer - '{offer}' on group '{disc_group}'"
                        )
                        # Remove group items from shopping list
                        for disc_item, disc_item_count in disc_group.items():
                            shopping_list[disc_item] -= disc_item_count
                            if shopping_list[disc_item] == 0:
                                del shopping_list[disc_item]
                        total += offer.price
                        break

            if num_items_to_qualify > 0:
                # deal could not be found
                return total

        return total
