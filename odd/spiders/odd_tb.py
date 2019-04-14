# -*- coding: utf-8 -*-
import scrapy
import json, re
from datetime import datetime, timedelta

from odd.head import params, cookies, shop
from odd.items import OddItem


class OddTbSpider(scrapy.Spider):
    name = 'odd_tb'
    allowed_domains = ['taobao.com', 'tmall.com']
    url = 'https://trade.taobao.com/trade/itemlist/asyncSold.htm?event_submit_do_query=1&_input_charset=utf8'
    pageSize = 100

    def start_requests(self):
        now = datetime.now()
        # params['dateBegin'] = str(1483200000000)
        datesAgo = now - timedelta(days=1)
        begin = datetime.timestamp(datesAgo) * 1000
        params['dateBegin'] = str(int(begin))
        params['dateEnd'] = str(int(now.timestamp()) * 1000 -1000)
        params['pageSize'] = str(self.pageSize)
        yield scrapy.FormRequest(self.url, callback=self.parse, method='POST', formdata=params, cookies=cookies)

    def parse(self, response):
        print('end time ', params['dateEnd'])
        datas = json.loads(response.text)
        pages = int(round(datas['page']['totalNumber'] / self.pageSize, 0))
        currentPage = int(datas['page']['currentPage'])
        print('总共', str(pages), '页', 'currentPage is ', str(currentPage))
        mainOrders = datas['mainOrders']
        print('获取数量', len(mainOrders))
        for mainOrder in mainOrders:
            item = OddItem()
            item['_id'] = id = mainOrder['id']
            item['actualFee'] = mainOrder['payInfo']['actualFee']
            item['status'] = mainOrder['statusInfo']['text']
            item['sellerFlag'] = mainOrder['extra']['sellerFlag']
            if item['status'] == '交易成功':
                try:
                    item['url'] = 'https:' + mainOrder['payInfo']['operations'][0]['url']
                except KeyError as e:
                    item['url'] = 'error'
            else:
                item['url'] = 'error'
            item['quantity'] = mainOrder['subOrders'][0]['quantity']
            item['nick'] = mainOrder['buyer']['nick']
            item['createTime'] = mainOrder['orderInfo']['createTime']
            item['shop'] = shop
            yield item

            url_detail = "https://trade.tmall.com/detail/orderDetail.htm?bizOrderId={}".format(id)
            yield scrapy.Request(url_detail, cookies=cookies, meta={'item': item}, callback=self.parse_detail)

        if currentPage < pages:
            params['pageNum'] = str(int(params['pageNum']) + 1)
            yield scrapy.FormRequest(self.url, callback=self.parse, method='POST', formdata=params, cookies=cookies)
        #"""

    def parse_detail(self, resp):
        item = resp.meta['item']
        r = re.search('detailData = (.*?)\n </script>', resp.text, re.S)
        # get order detail data
        data = json.loads(r.group(1))

        try:
            remark = data['overStatus']['operate'][1]['content'][0]['text']
            r = re.search('备忘：</span><span>(.*?)</span>', remark, re.S)
            mark = r.group(1)
            if '纸票' in mark:
                for i, v in enumerate(c[1:8]):
                    keys = ['买家留言', '发票抬头', '买家税号', '发票类型', '发票内容', '订单编号']
                    if v['key'] in keys:
                        if '发票类型' == v['key']:
                            print('去拒绝电子，因申请了电子票与纸票')
                            print(i, v['key'], v['content'][0]['text'])
                print('备忘：', mark)
            else:
                print('不用开纸票')
        except IndexError as e:
            print(id, 'no mark')
        yield item
