import scrapy

class UolScrapy(scrapy.Spider):
    
    name = 'Uol'
    start_urls = {
        'https://www.uol.com.br/'
    }

    def parse(self, response):
        cotacoes = response.xpath('//*[@id="HU_header"]/div[2]/div/div[2]/div[2]/ul/li[1]/a/span[2]/text()')
        print("cotacao: {}".format(len(cotacoes)))
        for cotacao in cotacoes:
            conteudo = cotacao.extract().strip()
            if conteudo != "":
                yield {
                    'A cotação atual do dólar é: ': conteudo
                }