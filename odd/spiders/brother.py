# -*- coding: utf-8 -*-
import scrapy
import json, re
from datetime import datetime as d, timedelta

from odd.head import params, all_cookies, gc
from odd.items import InvoiceItem


class BrotherSpider(scrapy.Spider):
    name = 'brother'
    allowed_domains = ['taobao.com', 'tmall.com']
    url = 'https://trade.taobao.com/trade/itemlist/asyncSold.htm?event_submit_do_query=1&_input_charset=utf8'
    pageSize = 100
    # shops = ['通众易加专卖店', '亿维通众专卖店', '通众旗舰店']
    shops = ['通众旗舰店']

    def start_requests(self):
        now = d.now()
        day = 4
        h = 0
        datesAgo = now - timedelta(days=day)
        # now = now - timedelta(days=day-1)
        # now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        datesAgo = datesAgo.replace(hour=h, minute=0, second=0, microsecond=0)
        begin = d.timestamp(datesAgo) * 1000
        params['dateBegin'] = str(int(begin))
        params['dateEnd'] = str(int(now.timestamp()) * 1000)
        params['pageSize'] = str(self.pageSize)
        for shop, cookie in all_cookies.items():
            if shop in self.shops:
                self.shop = shop
                self.cookies = gc(cookie)
                yield scrapy.FormRequest(self.url, callback=self.parse, method='POST', formdata=params, cookies=self.cookies)

    def parse(self, response):
        print('end time ', d.fromtimestamp(int(params['dateEnd'])/1000))
        datas = json.loads(response.text)
        pages = int(round(datas['page']['totalNumber'] / self.pageSize, 0))
        currentPage = int(datas['page']['currentPage'])
        print(self.shop, '总共', str(pages), '页', 'currentPage is ', str(currentPage))
        mainOrders = datas['mainOrders']
        print('获取数量', len(mainOrders), '总数', datas['page']['totalNumber'])
        for mainOrder in mainOrders:
            item = InvoiceItem()
            item['_id'] = id = mainOrder['id']
            item['actualFee'] = float(mainOrder['payInfo']['actualFee'])
            item['status'] = mainOrder['statusInfo']['text']
            item['nick'] = mainOrder['buyer']['nick']
            s = mainOrder['orderInfo']['createTime']
            item['createTime'] = d.strptime(s, '%Y-%m-%d %H:%M:%S')
            item['shop'] = self.shop

            url_detail = "https://trade.tmall.com/detail/orderDetail.htm?bizOrderId={}".format(id)
            yield scrapy.Request(url_detail, cookies=self.cookies, meta={'item': item}, callback=self.parse_detail)

        # """
        if currentPage < pages:
            params['pageNum'] = str(int(params['pageNum']) + 1)
            yield scrapy.FormRequest(self.url, callback=self.parse, method='POST', formdata=params, cookies=self.cookies)
        # """

    def parse_detail(self, resp):
        item = resp.meta['item']
        r = re.search('detailData = (.*?)\n </script>', resp.text, re.S)
        # get order detail data
        data = json.loads(r.group(1))
        c = data['basic']['lists']
        try:
            express = data['orders']['list'][0]['logistic']['content'][0]
            item['mailNo'] = express['mailNo']
        except KeyError as e:
            item['mailNo'] = ''

        s = ''
        for i, v in enumerate(c[1:]):
            text = v['content'][0]['text']
            if v['key'] == '发票抬头':
                s += text
            elif v['key'] == '买家税号':
                s += '/' +text
        item['invoice'] = s
        print(s)
        item['msg'] = c[1]['content'][0]['text']
        try:
            remark = data['overStatus']['operate'][1]['content'][0]['text']
            r = re.search('备忘：</span><span>(.*?)</span>', remark, re.S)
            mark = r.group(1)
            item['mark'] = mark        
        except IndexError as e:
            item['mark'] = ''
        if item['invoice'] != '' and ('票' in item['msg'] or '纸票' in item['mark']):
            url_invoice = 'https://einvoice.taobao.com/api/invoice/list/apply?applyListType=1&tid={}'.format(item['_id'])
            item['reject'] = '不清楚'
            yield item
            # yield scrapy.Request(url_invoice, cookies=self.cookies, meta={'item': item}, callback=self.parse_invoice)
        elif '票' in item['msg'] or '纸票' in item['mark']:
            item['reject'] = '无申请'
            yield item

    def parse_invoice(self, r):
        item = r.meta['item']
        datas = json.loads(r.text)
        print(datas)
        total = datas['total']
        if total != 0:
            item['reject'] = 'no'
        else:
            item['reject'] = 'yes'
        yield item