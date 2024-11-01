# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadsFictionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    rank = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    average_rating = scrapy.Field()
    score = scrapy.Field()
    url = scrapy.Field()
    pass
