# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


class AmazonScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field(input_processor=MapCompose(remove_tags),
                             output_processor=TakeFirst())
    book_author = scrapy.Field(input_processor=MapCompose(remove_tags),
                               output_processor=TakeFirst())
    book_price = scrapy.Field(input_processor=MapCompose(remove_tags),
                              output_processor=TakeFirst())
    book_image_link = scrapy.Field(input_processor=MapCompose(remove_tags),
                                   output_processor=TakeFirst())
