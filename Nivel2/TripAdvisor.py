from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
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

  download_delay = 2

  rules = (
    Rule(
      LinkExtractor(
        allow = r'/Hotel_Review-'
      ), follow = True, callback='parse_hotel'
    )
  )