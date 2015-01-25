from scrapy.spider import BaseSpider
from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector

from digitSpider.items import digitSpiderItem

class digitSpider(BaseSpider):
	name = "dmoz.org"
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//ul/li')
		items = []
		for site in sites:
			item = digitSpiderItem()
			item['title'] = site.select('a/text()').extract()
			item['link'] = site.select('a/@href').extract()
			item['desc'] = site.select('text()').extract()
			items.append(item)
		return items
