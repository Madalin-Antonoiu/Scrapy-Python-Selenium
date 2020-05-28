import scrapy
class MySpider(scrapy.Spider):
    name = 'feed_exporter_test'
    # this is equivalent to what you would set in settings.py file
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'test.csv'
    }
    start_urls = ['http://stackoverflow.com/questions/tagged/scrapy']

    def parse(self, response):
        titles = response.xpath("//a[@class='question-hyperlink']/text()").extract()

        for i, title in enumerate(titles):
            yield {'index': i, 'title': title}