import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bn"
    start_urls = [
        'https://buffalonews.com/2020/03/18/whats-open-a-list-of-local-restaurants-open-for-takeout-and-delivery/',
    ]

    def parse(self, response):
        filename = 'bn.html'
        with open(filename, 'wb') as f:
            f.write(response.body)