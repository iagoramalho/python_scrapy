import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.shell import inspect_response

class MercadoLivreSpider(scrapy.Spider):
    name = "MercadoLivreSpider"

    def __init__(self, pesquisa=None, *args, **kwargs):
        super(MercadoLivreSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://lista.mercadolivre.com.br/%s' % pesquisa]

    def parse(self, response):
      #inspect_response(response, self)
      #open_in_browser(response)
      #result = response.xpath('/html/body/main/div[2]/div/section/ol/li')
      result = response.xpath('.//ol[contains(@class,"section") and contains(@class,"search-results")]/li')
      for i in result:
          nome = (i.xpath(
          './/h2/span[contains(@class,"main-title")]/text()').extract_first()).strip()
          preco_simbolo = (i.xpath('.//div/span[contains(@class, "price__symbol")]/text()').extract_first())
          preco_fracao = (i.xpath('.//div/span[contains(@class, "price__fraction")]/text()').extract_first())
          preco_decimal = (i.xpath('.//div/span[contains(@class, "price__decimals")]/text()').extract_first())
          
          if preco_decimal is None:
            preco_decimal = "00"
          
          preco = str(preco_simbolo) + " " + str(preco_fracao) + "," + str(preco_decimal)
          
          yield {
              'name': nome,
              'preco': preco
          }
      NEXT_PAGE_SELECTOR = '.andes-pagination__button--next  a ::attr(href)'
      next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
      if next_page:
          yield scrapy.Request(
              response.urljoin(next_page),
              callback=self.parse
          )