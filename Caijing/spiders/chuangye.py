# -*- coding: utf-8 -*-

'''
获取创业帮第一个界面新闻
http://www.cyzone.cn/category/8/
建议每个2个小时爬取一次更新内容
'''


import scrapy
from Caijing.items import CaijingItem


class ChuangyeSpider(scrapy.Spider):
    name = 'chuangye'
    allowed_domains = ['www.cyzone.cn']
    start_urls = ['http://www.cyzone.cn/category/8/']

    def parse(self, response):
        item = CaijingItem()
        # print(response.text)
        pra_list =  response.xpath('//div[@class="lfn-bar"]')
        print(len(pra_list))
        for x in pra_list:
            cjTitle = x.xpath('./div[@class="lfn-title"]/a/text()').extract()[0]
            cjData = x.xpath('./div[@class="lfn-des"]/text()').extract()[0].strip()

            cjTime = x.xpath('./div/div[@class="info-left pull-left"]/span[1]/text()').extract()
            if not cjTime:
                cjTime = '空'
            else:
                cjTime = cjTime[0]
            cjFrom = x.xpath('./div/div[@class="info-left pull-left"]/span[2]/text()').extract()
            if not cjFrom:
                cjFrom = '空'
            else:
                cjFrom = cjFrom[0]
            cjUrl = x.xpath('./div[@class="lfn-title"]/a/@href').extract()[0]

            item['cjTitle'] = cjTitle
            item['cjData'] = cjData
            item['cjTime'] = cjTime
            item['cjFrom'] = cjFrom
            item['cjUrl'] = cjUrl
            item['cjwebsite'] = 'cyb'
            yield item



            # print('*'*30)
            # print(cjData)
            # print(cjFrom)
            # print(cjTime)
            # print(cjTitle)
            # print(cjUrl)
            # print('*'*30)



