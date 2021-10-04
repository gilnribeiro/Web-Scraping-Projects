import scrapy
from ..items import AmazonScrapingItem
from scrapy.loader import ItemLoader

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011'
    ]

    def parse(self, response):

        for book in response.css('.s-border-bottom'):
            il = ItemLoader(item=AmazonScrapingItem(), selector=book)
            il.add_css('book_name', '.a-color-base.a-text-normal')
            il.add_css('book_author', '.a-color-secondary .a-row .a-size-base+ .a-size-base')
            il.add_css('book_price', '.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole , .a-price-decimal')
            il.add_css('book_image_link', '.s-image::attr(src)')

            yield il.load_item()

        next_page = response.css('.a-last a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            # yield response.follow(next_page, callback=self.parse)

