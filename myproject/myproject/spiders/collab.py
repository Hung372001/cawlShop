import scrapy
from scrapy.selector import Selector
import re


class QuotesSpider(scrapy.Spider):
    name = "collab"
    start_urls = ["https://dirtycoins.vn/collab-s"]

    def parse(self, response):
        list_category = ['T-shirt','Pol-shirt','Shirt','SWEATERS','CARDIGANS','Bag','Jacket','Pack','Hoodie','Beanie','Combo','Jersey','Patch '
            ,'PANTS','Shorts','DRESSES','SKIRTS','Backpack','CROSSBODY BAGS','BOWLER BAGS','Cap','HATS','SLIDES','WALLETS','UNDERWEAR','MASKS','Jeans' ]

        for res in response.css("div.single-product"):
            img = res.css("img.lazyload::attr(src)").get()
            title = res.css("div.product-content>h3>a::text").get()
            price = res.css("span.regular-price::text").get()
            category = None
            for word in list_category:
                if word in title:
                    category = word



            item = {}
            item['img'] = img
            item['title'] = title
            item['price'] = price
            item['category'] = category
            yield item



