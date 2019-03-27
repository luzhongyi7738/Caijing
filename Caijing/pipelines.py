# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from  Caijing.settings import *



# 测试打印
class CaijingPipeline(object):
    def process_item(self, item, spider):
        # if item['cjwebsite'] == 'cyb':
        #     print('来自创业邦的信息*'*30)
        #     print(item['cjTitle'])
        #     # print(item['cjData'])
        #     print(item['cjTime'])
        #     print(item['cjFrom'])
        #     print(item['cjUrl'])
        #     print('*'*30)
        # elif item['cjwebsite'] == '36ke':
        #     print('来自36氪的信息*'*30)
        #     print(item['cjTitle'])
        #     # print(item['cjData'])
        #     print(item['cjTime'])
        #     print(item['cjFrom'])
        #     print(item['cjUrl'])
        #     print('*'*30)

        return item


class mongoPipeline(object):
    def __init__(self):
        #
        self.conn = pymongo.MongoClient(
            host=MONGODB_HOST,
            port=MONGODB_PORT,
        )
        # 库对象
        self.db = self.conn[MONGODB_DB]
        # 集合对象
        self.myset = self.db[MONGODB_SET]

    def process_item(self,item,spider):
        isSave = self.myset.find({'cjUrl':item['cjUrl']})
        if isSave.count() > 0:
            pass
        else:
            # 把item转为字典数据类型,利用dict方法
            d = dict(item)
            self.myset.insert_one(d)
        return item



