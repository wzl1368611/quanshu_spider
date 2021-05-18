# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanshuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    sort = scrapy.Field()
    novelname = scrapy.Field()
    novelimg = scrapy.Field()
    description = scrapy.Field()
    state = scrapy.Field()
    author = scrapy.Field()


class charpterItem(scrapy.Field):
    charpterid = scrapy.Field()
    novelid = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    novelname = scrapy.Field()
    sid = scrapy.Field()
