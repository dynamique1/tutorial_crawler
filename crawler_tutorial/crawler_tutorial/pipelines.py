# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging
# import pymongo
import sqlite3

# class MongodbPipeline:
#     collection_name = 'transcript'
#     def open_spider(self,spider):
#         self.client = pymongo.MongoClient("mongodb+srv://jimohabiodunn:Myheartbit@cluster0.5iyjkjt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#         self.db = self.client['My_DataBase']

    
#     def close_spider(self,spider):
#         self.client.close()


    
#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(item)
#         return item
    
class SQLitePipeline:
    
    def open_spider(self, spider):
        try:
            self.connection = sqlite3.connect('transcripts.db')
            self.c = self.connection.cursor()
            self.c.execute('''
                CREATE TABLE transcripts(
                    Title TEXT,
                    Plot TEXT,
                    Transcript TEXT,
                    Url TEXT
                )
            ''')
            self.connection.commit()
        except sqlite3.OperationalError as e:
            print("Error creating table:", e)
    
    def close_spider(self, spider):
        self.c.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO transcripts (Title, Plot, Transcript, Url) VALUES (?, ?, ?, ?)
        ''', (
            item.get('Title'),
            item.get('Plot'),
            item.get('Transcript'),
            item.get('Url'),
        ))
        self.connection.commit()
        return item