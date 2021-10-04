# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScrapytilesPipeline:
    def __init__(self):
        # Create or connect to database
        self.con = sqlite3.connect('mtiles.db')
        # Have open up and create cursor
        self.cur = self.con.cursor()
        # Create table if it doesn't already exist
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
        sku REAL PRIMARY KEY,
        name TEXT,
        price REAL
        )""")

    def process_item(self, item, spider):
        # This prevents adding multiple instances of the same data
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES (?,?,?)""", 
                            (item['sku'], item['name'], item['price']))
        # Commit changes to database
        self.con.commit()
        return item
