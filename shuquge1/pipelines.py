# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


class Shuquge1Pipeline:
    def __init__(self):
        self.content_list = []

    def process_item(self, item, spider):
        # item['chapter_num'] = '第' + str(item['chapter_num']) + '章'
        # item['chapter_title'] = ''.join(item['chapter_title'])
        self.content_list.append(item)
        return item

    # def open_spider(self, spider):
    #     pass

    def close_spider(self, spider):
        list_sorted = sorted(self.content_list, key=lambda x: x['chapter_num'])
        base_dir = os.getcwd()
        file_name = base_dir + r'\xiaoshuo.txt'
        f = open(file_name, 'a+', encoding='utf-8')
        for li in list_sorted:
            title = '第' + str(li['chapter_num']) + '章'
            f.write(title + '    ')
            f.write(''.join(li['chapter_title']))
            f.write(''.join(li['chapter_content']).replace('\xa0\xa0\xa0\xa0','\n\n') + '\n')
            f.write('\n')
        f.close()
