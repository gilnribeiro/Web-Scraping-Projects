import scrapy
from ..items import ScrapytilesItem
from scrapy.loader import ItemLoader

# to initiate terminal: scrapy shell link_of_webpage
# to run the scraper: scrapy crawl tiles (or the name of the spider, this file)
# to crawl, exit the shell (ctrl+C) and get into the scrapytiles (in this case) folder and run: scrapy crawl tiles
class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['http://magnatiles.com/products/page/1/']

    def parse(self, response):

        for p in response.css('ul.products li'): 
            il = ItemLoader(item=ScrapytilesItem(), selector=p) 

            il.add_css('sku', 'a.button::attr(data-product_sku)')
            il.add_css('name', 'h2')
            il.add_css('price', 'span.price bdi')

            yield il.load_item()

            # yield {                      
            #     'name' : p.css('h2::text').get(),
            #     'sku' : p.css('a.button::attr(data-product_sku)').get(),
            #     'price' : p.css('span.price bdi::text').get(),
            # }
        
        # We're looking for this link, inside the a tag, if it doesn't exist
        # it will go back to the next function
        next_page = response.css('ul.page-numbers a.next::attr(href)').get()
        if next_page is not None: 
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)