# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
class CharpterSpider(scrapy.Spider):
    name = 'charpter'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']
    link = LinkExtractor(allow=r'')
    def parse(self, response):
        pass
