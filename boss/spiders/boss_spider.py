# -*- coding: utf-8 -*-
import scrapy


class BossSpiderSpider(scrapy.Spider):
    name = 'boss_spider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101210100-p100103']

    def parse(self, response):
        pass
