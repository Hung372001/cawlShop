import scrapy
from scrapy.selector import Selector

class QuotesSpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://dirtycoins.vn/shop"]

    def parse(self, response):
        for item in response.css("div.single-product"):

              image = item.css("img.lazyload::attr(src)").get()
              title = item.css("div.product-content>h3>a::text").get()
              price = item.css("span.regular-price::text").get()
              yield {
                "image": image,
                "title": title,
                "price":price
              }

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)