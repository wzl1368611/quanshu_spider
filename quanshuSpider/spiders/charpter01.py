# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quanshuSpider.items import QuanshuspiderItem, charpterItem


class Charpter01Spider(CrawlSpider):
    name = 'charpter01'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://www.quanshuwang.com/book/0/312']
    # 盗墓笔记
    # 'http://www.quanshuwang.com/book/75/75690/22787538.html'
    # 'http://www.quanshuwang.com/book/195/195163'
    link = LinkExtractor(allow=r'http://www.quanshuwang.com/list/\d+\_\d+\.html')

    link_detail = LinkExtractor(allow=r'http://www.quanshuwang.com/book\_/d+\.html')
    # 该小说的基本内容
    # http://www.quanshuwang.com/book_9055.html
    link_charpter = LinkExtractor(allow=r'http://www.quanshuwang.com/book/\d+/\d+')
    # 'http://www.quanshuwang.com/book/75/75690'
    # 此为章节目录内容

    link_content = LinkExtractor(allow=r'http://www.quanshuwang.com/book/\d+/\d+/\d+\.html')
    # 该小说的章节内容
    # http://www.quanshuwang.com/book/9/9055/9674264.html

    # http://www.quanshuwang.com/book/9/9055
    # 该小说的章节目录
    rules = (
        # Rule(link, callback='parse_item', follow=False),
        # Rule(link_detail, callback='parse_detail'),
        # Rule(link_charpter,callback='parse_charpter',follow=True),
        Rule(link_content, callback='parse_content'),
    )

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        local_url = response.url
        types = local_url.split('_')[0].split('/')[-1]

        # print('类别是：', types)
        sort = response.xpath('//*[@id="navList"]/div/a[2]/text()').extract_first()
        # print('分类是：', sort)

        # soup.select('.section.board-list.board-list-collapse ul li')
        detail_lists = response.xpath('//section[@class="section board-list board-list-collapse"]/ul/li')
        # '//section[@class="section board-list board-list-collapse"]/ul/li'
        # print('-----> ？？？？？？？？？？？？？？？？？？？？？？？？')
        # print(detail_lists)
        for detail in detail_lists:
            item = QuanshuspiderItem()
            item["type"] = types
            item['sort'] = sort
            novelimg = detail.xpath('./a/img/@src').extract_first()
            item["novelimg"] = novelimg
            # '//*[@id="navList"]/section/ul/li[32]/a/img'
            novelname = detail.xpath('./span/a[1]/@title').extract_first()
            item["novelname"] = novelname
            # '//*[@id="navList"]/section/ul/li[32]/span/a[1]'
            href = detail.xpath('./a/@href').extract_first()
            # '//*[@id="navList"]/section/ul/li[32]/a'
            author = detail.xpath('./span/a[2]/text()').extract_first()
            item["author"] = author
            # '//*[@id="navList"]/section/ul/li[32]/span/a[2]'
            state = detail.xpath('./img[@class="topss png_bg"]/@src').extract_first()
            # item["state"] = state
            # '//*[@id="navList"]/section/ul/li[32]/img'
            # print('图片:', novelimg)
            # print('小说名称：', novelname)
            # print('链接：', href)
            print('作者是：', author)
            if 'only2.png' in state:
                state = '连载中'
            else:
                state = '完结'
            item["state"] = state
            print('状态是：', state)
        # return item
    def parse_detail(self,response):
        description = response.xpath('//*[@id="waa"]/text()').extract_first()
        print('简介是：',description)
    def parse_charpter(self,response):
        charpter_lists = response.xpath('//*[@id="chapter"]/div[4]/div[3]/ul/div[2]/li')
        # '//*[@id="chapter"]/div[3]/div[3]/ul/div[2]/li[4]/a'
        # name = response.xpath('//*[@id="chapter"]/div[4]/div[1]/strong').extract_first()
        for charpter_list in charpter_lists:
            # item = charpterItem()
            # link = charpter_list.xpath('./a/@href').extract_first()
            title = charpter_list.xpath('./a/text()').extract_first()
            print('小说章节是：', title)
    def parse_content(self, response):
        now_url = response.url
        sid = now_url.split('.')[-2].split('/')[-1]
        print('当前的url是：', now_url)
        name = response.xpath('//*[@id="directs"]/div[1]/h1/em/text()').extract_first()
        new_name = name.split('《')[1].split('》')[0]
        title = response.xpath('//*[@id="directs"]/div[1]/h1/strong/text()').extract_first()
        content = response.xpath('//*[@id="content"]/text()').extract()
        # '//*[@id="content"]'
        content = ''.join(content)
        content = content.replace('"', '')
        print('----->小说名称',new_name)
        print('----->小说章节',title)
        # print('----->小说内容',content)
        item = charpterItem()
        item['title'] = title
        item['content'] = content
        item['novelname'] = name
        item['novelid'] = 1
        item['sid'] = int(sid)
        yield item



