# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join ,Compose

class StripText:
    def __init__(self, chars=' \r\t\n'):
        self.chars = chars

    def __call__(self, value): 
    	try: 	
            return value.strip(self.chars)
        except:
            return value

def str_to_int(x):
    try:
        return int(float(x))
    except:
        return x


class SteamItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItem(scrapy.Item):
    app_name = scrapy.Field()  # (1)
    specs = scrapy.Field(
        output_processor=MapCompose(StripText())  # (4)
    )
    n_reviews = scrapy.Field(
        output_processor=Compose(
            MapCompose(
                StripText(), 
                lambda x: x.replace(',', ''), 
                str_to_int),  # (5)
            max
        )
    )

class ProductItemLoader(ItemLoader):
    default_output_processor=TakeFirst()  # (2)


