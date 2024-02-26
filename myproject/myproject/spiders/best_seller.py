import scrapy
from scrapy.selector import Selector
import re


class QuotesSpider(scrapy.Spider):
    name = "best_seller"
    start_urls = ["https://dirtycoins.vn/tops",
                  "https://dirtycoins.vn/bottoms",
                  "https://dirtycoins.vn/bags",
                  "https://dirtycoins.vn/womenswear",
                  "https://dirtycoins.vn/restocks",
                  "https://dirtycoins.vn/combo",
                  "https://dirtycoins.vn/best-seller"]

    def parse(self, response):
        list_category = ['T-shirt','Pol-shirt','Shirt','SWEATERS','CARDIGANS','Bag','Jacket','Pack','Hoodie','Beanie','Combo','Jersey','Patch '
            ,'PANTS','Shorts','DRESSES','SKIRTS','Backpack','CROSSBODY BAGS','BOWLER BAGS','Cap','HATS','SLIDES','WALLETS','UNDERWEAR','MASKS','Jeans','Cardigan','Slides','Polo', 'Pants','Cardigan','Polo','Slides','Pin','Sweatshirt','Sweater','Skirt','Crop Top','Briefs','Bra']

        for res in response.css("div.single-product"):
            li_element=res.css("div.product-img.img-full>a>ul>li::text").get()
            img = res.css("img.lazyload::attr(src)").get()
            title = res.css("div.product-content>h3>a::text").get()
            price = res.css("span.regular-price::text").get()
            status="New arrival" if li_element and li_element.strip().lower()=='new arrival' else None
            category = None
            for word in list_category:
                if word in title:
                    category = word



            item = {}
            item['img'] = img
            item['title'] = title
            item['price'] = price
            item['category'] = category
            item['status']=status
            yield item
             


