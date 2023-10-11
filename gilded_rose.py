# -*- coding: utf-8 -*-

class Item:

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        '''
        This function initialise an object

        Parameters:
            name: object name
            sell_in: sold objects amount
            quality: object quality
        '''
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        '''
        This function returns object parameters

        Returns:
            str: object parameters
        '''
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


def update_quality(items: Item) -> Item:
    '''
    This function updates an item qualities

    Parameters:
        itens: number of items

    Returns:
        Item: updated items
    '''
    for item in items:
        if (item.name != "Aged Brie" and
            item.name != "Backstage passes to a TAFKAL80ETC concert"):
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1

                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1

                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1

        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    return items