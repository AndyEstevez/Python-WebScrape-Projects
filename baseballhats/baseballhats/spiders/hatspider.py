import scrapy

from baseballhats.items import BaseballhatsItem

class HatSpider(scrapy.Spider):
    name = 'hat'
    start_urls = ['https://www.mlbshop.com/new-york-mets/men-caps/t-36993297+ga-90+d-7850114425+z-9-2740874255?_ref=p-DLP:m-SIDE_NAV']

    def parse(self, response):
        for hat in response.css('div.column'):
            item = BaseballhatsItem()
            item['name'] = hat.css('div.product-card-title > a::attr(title)').get()
            item['price'] = hat.css('span.money-value > span.sr-only::text').get()
            item['url'] = "https://www.mlbshop.com" + hat.css('div.product-image-container > a::attr(href)').get()
            item['image_url'] = "http:" + hat.css('div.product-image-container > a > img::attr(src)').get()
            
            try: 
                if hat.css('div.flag.flag-orange::text').get():
                    item['stock'] = hat.css('div.flag.flag-orange::text').get()
                else:
                    item['stock'] = "In Stock"
            except: 
                item['stock'] = "In Stock"
            
            yield item
