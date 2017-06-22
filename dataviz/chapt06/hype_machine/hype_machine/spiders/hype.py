# run as scrapy runspider -t json -o hype.json hype.py

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://hypem.com/spy/RU']

    def parse(self, response):
        for title in response.css('h3.track_name'):
            yield {'artist': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

