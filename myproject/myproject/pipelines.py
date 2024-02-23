# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MyprojectPipeline:
    def process_item(self, item, spider):
        df = pd.DataFrame([item])  # Create a DataFrame from the item
        df.to_excel('data.xlsx', index=False)
