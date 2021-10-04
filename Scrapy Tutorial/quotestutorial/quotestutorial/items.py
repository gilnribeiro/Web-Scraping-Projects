# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data -> Temporary containers (items) -> Storing in database

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


class QuotestutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    quote = scrapy.Field(input_processor=MapCompose(remove_tags),
                         output_processor=TakeFirst())
    author = scrapy.Field(input_processor=MapCompose(remove_tags),
                          output_processor=TakeFirst())
    tags = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())



