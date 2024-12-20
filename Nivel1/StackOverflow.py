import requests
from bs4 import BeautifulSoup

headers = {
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://stackoverflow.com/questions"

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text, "html.parser")

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all('div', class_="s-post-summary")

# for pregunta in lista_de_preguntas:
#   texto_pregunta = pregunta.find('h3').text
#   descripcion_pregunta = pregunta.find(class_='s-post-summary--content-excerpt').text
#   #replace es una funcion para reemplazar, en este caso lo usariamos para los espacios y los saltos de linea
#   #strip elimina los espacios que estan antes o despues de una cadena
#   descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r','').strip()
#   print(texto_pregunta)
#   print(descripcion_pregunta)

#   print()

#Con beautifulsoup
for pregunta in lista_de_preguntas:
  elemento_texto_pregunta = pregunta.find('h3')
  texto_pregunta = elemento_texto_pregunta.text

  descripcion_pregunta = elemento_texto_pregunta.find_next_sibling('div').text
  
  #replace es una funcion para reemplazar, en este caso lo usariamos para los espacios y los saltos de linea
  #strip elimina los espacios que estan antes o despues de una cadena
  descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r','').strip()
  print(texto_pregunta)
  print(descripcion_pregunta)

  print()