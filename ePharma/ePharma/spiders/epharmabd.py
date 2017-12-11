# -*- coding: utf-8 -*-
import scrapy
from ePharma.items import ePharmaItem

class EpharmaSpider(scrapy.Spider):
    name = 'epharmabd'
    allowed_domains = ['epharma.com.bd']
    start_urls = [
	'http://epharma.com.bd/product-category/multivitamin',
	'http://epharma.com.bd/product-category/dental-oral-care/',
	'http://epharma.com.bd/product-tag/skin-care/',
	'http://epharma.com.bd/product-category/eye-ear-care/',
	'http://epharma.com.bd/product-category/diabetic-care/',
	'http://epharma.com.bd/product-category/herbal/',
	'http://epharma.com.bd/product-category/personal-care/',
	'http://epharma.com.bd/product-category/medicines/',

	]

    def parse(self, response):
		titles=response.css('.product-loop-title ::text').extract()
		urls=response.css('.product-loop-title ::attr(href)').extract()
		prices=response.css('.price ::text').extract()
		descriptions=response.css('.description ::text').extract()

		for ref in response.css('.product-type-simple'):
			item=ePharmaItem()
			item['title']=ref.css('.product-loop-title ::text').extract()
			item['url']=ref.css('.product-loop-title ::attr(href)').extract()
			item['price']=ref.css('.price ::text').extract()
			item['description']=ref.css('.description ::text').extract()
		
	#	for ind,ele in enumerate(titles):
	#		item=ePharmaItem()
	#		item['title']=titles[ind]
	#	#	print(item['title'])
	#		item['url']=urls[ind]
	#	#	print(item['url'])
	#		item['price']=prices[ind]
		#	print(item['price'])
	#		item['description']=descriptions[ind]
	#	#	print(item['description'])
			print(item)
			yield item 

		next_page=response.css('.next.page-numbers ::attr(href)').extract()[-1]

		print(next_page)
		if next_page:
			yield scrapy.Request(next_page, self.parse, dont_filter=True)


