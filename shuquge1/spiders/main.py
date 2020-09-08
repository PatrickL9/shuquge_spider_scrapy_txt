# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# if __name__ == '__main__':
#     process = CrawlerProcess(get_project_settings())
#     process.crawl('shuquge_crawl')
#     process.start()

from scrapy import cmdline

name = 'shuquge_crawl'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())