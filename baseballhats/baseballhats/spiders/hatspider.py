import scrapy

from baseballhats.items import BaseballhatsItem

class HatSpider(scrapy.Spider):
    name = 'hat'
    start_urls = ['https://www.mlbshop.com/new-york-mets/men-caps/t-36993297+ga-90+d-7850114425+z-9-2740874255?_ref=p-DLP:m-SIDE_NAV']