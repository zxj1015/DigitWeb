# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DigitspiderPipeline(object):
	def __init__(self):
		self.file = open('sample.txt', 'wb')
	def process_item(self, item, spider):
		self.file.write(item['title'] + '\t' + item['link'] + '\t' + item['desc'] + '\n')
    return item
