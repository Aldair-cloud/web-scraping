from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from itemloaders.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

class Hotel(Item):
  nombre = Field()
  precio = Field()
  descripcion = Field()
  amenities = Field()

class TripAdvisor(CrawlSpider):
  name = "Hoteles"
  custom_settings = {
    "USER-AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
  }

  start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

  # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
  allowed_domains = ['tripadvisor.com']

  download_delay = 2

  rules = (
    Rule(
      LinkExtractor(
        allow = r'/Hotel_Review-'
      ), follow = True, callback='parse_hotel'
    ),
  )

   # Funcion a utilizar con MapCompose para realizar limpieza de datos
  def quitarDolar(self, texto):
    return texto.replace("$", "")

    # Callback de la regla
  def parse_hotel(self, response):
    sel = Selector(response)

    item = ItemLoader(Hotel(), sel)
    item.add_xpath('nombre', '//h1[@id="HEADING"]/text()')
    item.add_xpath('precio', '//span[@class="aLfMd"]/text()',
                        MapCompose(self.quitarDolar)) # Debido a que ahora estamos obteniendo el score, no es necesario este post-procesamiento
    # Es posible utilizar Map Compose con funciones anonimas
    # PARA INVESTIGAR: Que son las funciones anonimas (lambda) en Python?
    item.add_xpath('descripcion', '//div[@class="fIrGe _T"]//text()', # //text() nos permite obtener el texto de todos los hijos
                       MapCompose(lambda i: i.replace('\n', '').replace('\r', '')))
    item.add_xpath('amenities',
                       '//div[contains(@data-test-target, "amenity_text")]/text()')
    yield item.load_item()