import requests
from lxml import html

encabezados = {
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezados)

parser = html.fromstring(respuesta.text)

#obtenemos el elemento por el id
#ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
#print(ingles)

# idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
# for idioma in idiomas:
#   print(idioma)

idiomas = parser.find_class('central-featured-lang')
for idioma in idiomas:
  print(idioma.text_content())
  