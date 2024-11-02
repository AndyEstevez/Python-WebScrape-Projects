import scrapy

from baseballhats.items import BaseballhatsItem

class HatSpider(scrapy.Spider):
    name = 'hat'
    start_urls = ['https://www.mlbshop.com/new-york-mets/men-caps/t-36993297+ga-90+d-7850114425+z-9-2740874255?_ref=p-DLP:m-SIDE_NAV']

    def log_error(self, failure): # handle errors
        self.logger.error(repr(failure))

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, errback=self.log_error)

    def parse(self, response): # handle scraping site for saving into Item
        for hat in response.css('div.column'):
            item = BaseballhatsItem()
            item['name'] = hat.css('div.product-card-title > a::attr(title)').get()
            item['price'] = hat.css('span.money-value > span.sr-only::text').get()
            item['url'] = "https://www.mlbshop.com" + hat.css('div.product-image-container > a::attr(href)').get()
            item['image_url'] = "http:" + hat.css('div.product-image-container > a > img::attr(src)').get()

            # edge case for if hat has "Low Stock"
            if hat.css('div.flag.flag-orange::text').get():
                item['stock'] = hat.css('div.flag.flag-orange::text').get()
            else:
                item['stock'] = "In Stock"
            
            yield item

        # checking for next page and loop until no more pages remain to scrape
        next_page_available = response.css('li.next-page > a::attr(aria-disabled)').get()
        if next_page_available == 'false':
            next_page = "https://www.mlbshop.com" + response.css('li.next-page > a::attr(href)').get()
            self.logger.info(f"Navigating to next page with URL {next_page}")
            yield response.follow(next_page, callback=self.parse, errback=self.log_error)