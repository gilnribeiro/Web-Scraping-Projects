# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo db
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import sqlite3
import mysql.connector



class QuotestutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # self.conn = sqlite3.connect('quotes_tb.db')
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='PlanetKepler1',
            database='myquotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table IF NOT EXISTS quotes_tb(
                            quote text,
                            author text, 
                            tags text
                            )""")

    def store_db(self, item):
        # This prevents adding multiple instances of the same data
        # self.curr.execute("""INSERT OR IGNORE INTO quotes_tb VALUES (?,?,?)""",
        #                   (item['quote'], item['author'], item['tags'],))
        self.curr.execute("""INSERT INTO quotes_tb VALUES (%s,%s,%s)""",
                          (item['quote'], item['author'], item['tags'],))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
