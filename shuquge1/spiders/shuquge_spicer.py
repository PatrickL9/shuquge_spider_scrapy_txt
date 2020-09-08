import re
from scrapy import Request
from scrapy.spiders import Spider
from ..items import Shuquge1Item

class Shuquge_Crawl(Spider):
    name = 'shuquge_crawl'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }


    def start_requests(self):
        url = 'http://www.shuquge.com/txt/6356/index.html'
        yield Request(url, headers=self.headers)


    def parse(self, response):
        chapter_urls = response.xpath('//div[@class="listmain"]/dl/dd')
        i = 0
        j = 0
        for url in chapter_urls:
            # 前12个章节是重复的，去掉，从第13条连接开始是小说第一章
            i += 1
            if i > 12:
                j += 1
                temp_url = url.xpath('.//a/@href').extract()
                temp_url_com = 'http://www.shuquge.com/txt/6356/' + re.sub('\[\'|\'\]','',str(temp_url))
                yield Request(temp_url_com, callback=lambda response, chap=j: self.get_content(response, chap))


    def get_content(self, response, chap):
        item = Shuquge1Item()
        item['chapter_num'] = chap
        item['chapter_title'] = response.xpath('//div[@class="content"]/h1/text()').extract()
        temp_content = response.xpath('//div[@class="content"]/div[@id="content"]/text()').extract()
        item['chapter_content'] = temp_content
        yield item