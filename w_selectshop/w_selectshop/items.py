# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WSelectshopItem(scrapy.Item):
    brand = scrapy.Field()
    target = scrapy.Field()
    product = scrapy.Field()
    explain = scrapy.Field()
    origin_price = scrapy.Field()
    now_price = scrapy.Field()
    star_score = scrapy.Field()
    code = scrapy.Field()
    material = scrapy.Field()
    firm_madein = scrapy.Field()
    material2 = scrapy.Field()
    firm_import = scrapy.Field()
    made_in = scrapy.Field()
    birth = scrapy.Field()
    image_link = scrapy.Field()
