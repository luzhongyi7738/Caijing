# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaijingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cjTitle = scrapy.Field()
    cjData = scrapy.Field()
    cjTime = scrapy.Field()
    cjFrom = scrapy.Field()
    cjUrl = scrapy.Field()
    cjwebsite = scrapy.Field()


class SanliuItem(scrapy.Item):
    cjTitle = scrapy.Field()
    cjData = scrapy.Field()
    cjTime = scrapy.Field()
    cjFrom = scrapy.Field()
    cjUrl = scrapy.Field()
    cjwebsite = scrapy.Field()



