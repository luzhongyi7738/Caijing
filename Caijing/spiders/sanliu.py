# -*- coding: utf-8 -*-
import scrapy
from Caijing.items import SanliuItem



class SanliuSpider(scrapy.Spider):
    name = 'sanliu'
    allowed_domains = ['36kr.com']

    start_urls = ['https://36kr.com/information/contact']

    # start_urls = ['https://36kr.com/p/5188676']

    # 根据首页解析出每条的url 再进一步爬
    def parse(self, response):
        r_list = response.xpath('//div[@class="information-flow-item"]')
        print(len(r_list))
        for r in r_list:
            url = r.xpath('.//a[@class="article-item-pic"]/@href').extract()[0]
            url = 'https://36kr.com' + url
            print(url)
            yield scrapy.Request(url,callback=self.parse_infos)



    def parse_infos(self,response):
        # print(response.text)
        item = SanliuItem()
        res = response.xpath('//div[@class="article-wrapper common-width"]')[0]
        cjTitle = res.xpath('./div[@class="common-width"]/div/h1/text()').extract()
        # print(cjTitle)


        # 获取有多少p标签,并获取所有text内容
        cjData = []
        data = res.xpath('./div[2]/div/p').extract()
        for i in range(1,len(data)+1):
            temp = res.xpath('./div[2]/div/p[%d]'%i)
            temp_1 = res.xpath('./div[2]/div/p[%d]/text()'%i).extract()
            temp_2 = temp.xpath('string(.)').extract()[0]
            cjData.append(temp_2)
            # try:
            #     h1 = temp.xpath('./h1/text()')[0]
            #     print("h1:",h1)
            # except:
            #     pass
            # try:
            #     h2 = temp.xpath('./h2/text()')[0]
            #     print("h2:",h2)
            # except:
            #     pass
            # try:
            #     h3 = temp.xpath('./h3/text()')[0]
            #     print("h3:",h3)
            # except:
            #     pass
            try:
                img = temp.xpath('./img/@src').extract()[0]
                cjData.append(img)
            except:
                pass
        # print(cjData.__len__())

        # 获取div下所有h3标签的文本内容
        h3 = res.xpath('./div[2]/div/h3').extract()
        if len(h3)> 0:
            for i in range(1,len(h3)+1):
                smalltitle = res.xpath('./div[2]/div/h3[%d]'%i)
                smalltitle =smalltitle.xpath('string(.)').extract()[0]
                smalltitle = 'smalltitle:' + smalltitle
                cjData.append(smalltitle)
        else:
            pass
        # 作者
        cjFrom = res.xpath('./div[1]/div[1]/div/a/text()').extract()[0]
        # 原文url
        cjUrl = response.url
        cjTime = 'null'


        item['cjTitle'] = cjTitle
        item['cjData'] = cjData
        item['cjTime'] = cjTime
        item['cjFrom'] = cjFrom
        item['cjUrl'] = cjUrl
        item['cjwebsite'] = '36ke'
        yield item


















