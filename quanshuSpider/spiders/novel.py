# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
from quanshuSpider.items import QuanshuspiderItem, charpterItem


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']

    def parse(self, response):
        li_lists = response.xpath('//*[@id="channel-header"]/div/nav/ul/li')
        for li in li_lists:
            url = li.xpath('./a/@href').extract_first()
            sort = li.xpath('./a/text()').extract_first()
            print('类型：', url)
            print('分类：', sort)
            yield scrapy.Request(url=url, callback=self.detail_parse)

    def detail_parse(self, response):

        last_page = response.xpath('//*[@id="pagelink"]/a[@class="last"]/text()').extract_first()
        print('最后一页的页码是：', last_page)
        if last_page:
            last_href = response.xpath('//*[@id="pagelink"]/a[@class="last"]/@href').extract_first()
            basic_href = last_href.split('_')[0]
            page = int(last_page)
            # for i in range(1, page + 1):
            for i in range(1, 3):
                new_url = basic_href + f'_{i}.html'
                print('新的url是：', new_url)
                yield scrapy.Request(url=new_url, callback=self.detail_content_parse)

    def detail_content_parse(self, response):
        # '//*[@id="navList"]/section/ul/li[2]'
        # print(response.text)
        # detail_lists = response.xpath('//section[@class="section.board-list.board-list-collapse"]/ul/li')
        # with open('aaa.html', 'w') as f:
        #     f.write(response.text)
        #     print('写入ok!')
        # print(response.text)
        # soup = BeautifulSoup(response.text, 'html.parser')

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
            yield scrapy.Request(url=href, meta={'item': item}, callback=self.desp_parse)

    def desp_parse(self, response):
        item = response.meta['item']
        description = response.xpath('//*[@id="waa"]/text()').extract_first()
        item["description"] = description
        # //*[@id="waa"]
        print('简介：', description)
        charpter_url = response.xpath('//*[@id="container"]/div[2]/section/div/div[1]/div[2]/a[1]/@href').extract_first()
        print('-----> 章节的url是：',charpter_url)
        # '//*[@id="container"]/div[2]/section/div/div[1]/div[2]/a[1]'
        yield scrapy.Request(url=charpter_url, callback=self.charpter_parse)

        yield item

    def charpter_parse(self, response):
        charpter_lists = response.xpath('//*[@id="chapter"]/div[4]/div[3]/ul/div[2]/li')
        name = response.xpath('//*[@id="chapter"]/div[4]/div[1]/strong').extract_first()
        for charpter_list in charpter_lists:
            item = charpterItem()
            link = charpter_list.xpath('./a/@href').extract_first()
            title = charpter_list.xpath('./a/text()').extract_first()
            item['title'] = title
            item['novelname'] = name
            item['novelid'] = 1
            print('-----> 章节主题：', title)
            print('-----> 章节小说名称：', name)
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.charpter_content_parse)

    def charpter_content_parse(self, response):
        item = response.meta['item']
        # '//*[@id="content"]/div'
        content = response.xpath('//*[@id="content"]/div/text()').extract()
        # '//*[@id="content"]/div'
        item['content'] = ''.join(content)
        # print('-----> 章节内容是', item['title'])
        yield item
