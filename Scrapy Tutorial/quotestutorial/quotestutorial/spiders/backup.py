# import scrapy
# from ..items import QuotestutorialItem
# from scrapy.loader import ItemLoader
#
#
# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     # allowed_domains = ['quotes.toscrape.com']
#     start_urls = [
#         'https://quotes.toscrape.com/'
#     ]
#
#     def parse(self, response):
#
#         all_div_quotes = response.css('div.quote')
#         for q in all_div_quotes:
#             il = ItemLoader(item=QuotestutorialItem(), selector=q)
#
#             il.add_css('quote', 'span.text')
#             il.add_css('author', 'small.author')
#             il.add_css('tags', '.tags a')
#
#             yield il.load_item()
#
#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
#             # yield response.follow(next_page, callback=self.parse)
