from urllib import response
import scrapy


class AthleticsSpider(scrapy.Spider):
    name = "athletics"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/1992_World_Junior_Championships_in_Athletics_–_Men%27s_high_jump"]

    def parse(self, response):
        
        table = response.xpath('//table')[1].xpath('tbody/tr')

        for tr in table:
            yield {
                "medal": tr.xpath('td/b/text()').get(),
                "athlete": tr.xpath('td/a/text()').get()
            }
