import scrapy

class TerraSpider(scrapy.Spider):

    name = 'Terra'
    start_urls = {
        'https://www.terra.com.br/'
    }

    def parse(self, response):
        titulos = response.css(".main-url::text")
        #titulos = response.xpath('//*[contains(@class, "main-url")]/text()')
        print("titulos: {}".format(len(titulos)))
        for titulo in titulos:
            conteudo = titulo.extract().strip()
            if conteudo != "":
                yield {
                    'titulo': conteudo
                }