# -*- coding: utf-8 -*-
import pymongo
from logging import getLogger
from scrapy.conf import settings

logger = getLogger(__name__)

class MongoDBPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        self.stats = stats
        self.stats.set_value('MongoDB/stored', 0)

    def open_spider(self, spider):
        server = settings.get('MONGO_SERVER')
        port = settings.get('MONGO_PORT')
        database = settings.get('MONGO_DATABASE')
        self.collection = spider.uid
        self.conn = pymongo.MongoClient(server, port)
        self.db = self.conn[database]
        logger.info('Conected with MongoDB on {} database.'.format(database))

    def process_item(self, item, spider):
        self.db[self.collection].insert_one(dict(item))
        self.stats.inc_value('MongoDB/stored')

    def close_spider(self, spider):
        self.conn.close()
        logger.info('Closed connection with MongoDB.')
