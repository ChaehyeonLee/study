# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['engadget.com']
    start_urls = ['http://engadget.com/']

    def parse(self, response):
        pass
