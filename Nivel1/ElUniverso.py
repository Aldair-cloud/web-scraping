from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class Noticia(Item):

  titular = Field()
  despcripcion = Field()

class ElUniversoSpider(Spider):
  name = 'MiSegundoSpider'
  custom_settings = {
    "USER-AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
  }

  start_urls = ['https://www.eluniverso.com/deportes/']

  def parse(self, response):
    sel = Selector(response)
    noticias = sel.xpath('//div[contains(@class="content-feed")]/ul/li')

    for noticia in noticias:
      pass
