import scrapy
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://dirtycoins.vn/shop"]

    def parse(self, response):
        for res in response.css("div.single-product"):
            img = res.css("img.lazyload::attr(src)").get()
            title = res.css("div.product-content>h3>a::text").get()
            price = res.css("span.regular-price::text").get()
            item = {}
            item['img'] = img
            item['title'] = title
            item['price'] = price
            yield item

# next_page = response.css("li.next a::attr(href)").get()
# if next_page is not None:
#     yield response.follow(next_page, self.parse)
