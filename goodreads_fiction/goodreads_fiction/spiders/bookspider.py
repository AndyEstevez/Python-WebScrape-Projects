import scrapy

from goodreads_fiction.items import GoodreadsFictionItem

class BookSpider(scrapy.Spider):
    name = 'book'
    start_urls = ['https://www.goodreads.com/list/show/1.Best_Books_Ever']

    def parse(self, response):
        base_url = 'https://www.goodreads.com'

        for booklist in response.css('tr[itemtype="http://schema.org/Book"]'):
            item = GoodreadsFictionItem()
            item['rank'] = booklist.css('td.number::text').get()
            item['title'] = booklist.css('span[itemprop="name"][role="heading"]::text').get()
            item['author'] = booklist.css('a.authorName > span::text').get()
            item['average_rating'] = booklist.css('span.minirating::text').get()[1:5] + "/5.00"
            item['score'] = booklist.css('a[href="#"][onclick^="Lightbox"]::text').get()[7:]
            item['url'] = base_url + booklist.css('a.bookTitle::attr(href)').get()
            yield item

        next_page = base_url + response.css('a.next_page').attrib['href']
        next_page_num = int(response.css('a.next_page').attrib['href'][-1])-1
        # stops after page 10 
        if next_page is not None and next_page_num != 0:
            yield response.follow(next_page, callback=self.parse)