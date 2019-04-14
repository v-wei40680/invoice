# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class OddPipeline(object):
    def __init__(self):
        s = settings
        self.client = pymongo.MongoClient(host=s['MONGO_HOST'], port=s['MONGO_PORT'])
        self.db = self.client[s['MONGO_DB']]
        self.coll = self.db[s['MONGO_COLL']]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.coll.save(postItem)
        return item

class InvoicePipeline(object):
    def __init__(self):
        s = settings
        self.client = pymongo.MongoClient(s['URI'])
        self.db = self.client[s['MONGO_DB']]
        self.coll = self.db[s['MONGO_COLL2']]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.coll.save(postItem)
        return item
