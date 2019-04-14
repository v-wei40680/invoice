# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OddItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    actualFee = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()
    quantity = scrapy.Field()
    nick = scrapy.Field()
    createTime = scrapy.Field()
    shop = scrapy.Field()
    express = scrapy.Field() 
    mailNo = scrapy.Field() 
    sellerFlag = scrapy.Field() 

class InvoiceItem(scrapy.Item):
    _id = scrapy.Field()
    actualFee = scrapy.Field()
    status = scrapy.Field()
    nick = scrapy.Field()
    createTime = scrapy.Field()
    shop = scrapy.Field()
    mailNo = scrapy.Field()
    reject = scrapy.Field()
    msg = scrapy.Field()
    invoice = scrapy.Field()
    mark = scrapy.Field()
