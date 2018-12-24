from doe_sangue.items import HemopeItem
import scrapy


class HemopeSpider(scrapy.Spider):
    name = 'hemope'
    allowed_domains = ['www.hemope.pe.gov.br']
    start_urls = ['http://www.hemope.pe.gov.br/']

    def parse(self, response):
        for tipo_sangue in response.xpath('//ul[contains(\
         @class,"list-estoque")]/li'):

            item = HemopeItem()

            item['url'] = response.url

            item['banco'] = "HEMOPE"

            item['tipo_sangue'] = tipo_sangue.xpath(
                './/strong/text()').extract_first()

            item['nivel_sangue'] = tipo_sangue.xpath(
                './/div[contains(@class,"bolsa")]/div[2]/@class'
                ).re_first(r'sangue\s*(.*)')

            yield item
