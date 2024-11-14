import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'

headers = {
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

respuesta = requests.get(url, headers=headers)

#para obtener el texto en crudo del HTML
soup = BeautifulSoup(respuesta.text, 'lxml')

lista_noticias = soup.find_all('tr', class_='athing')

for noticia in lista_noticias:
  titulo = noticia.find('span', class_='titleline').text

  url = noticia.find('span', class_='titleline').find('a').get('href')

  #recorrer el arbol de otra manera(para buscar como hermanos)
  metadata = noticia.find_next_sibling()

  score = 0
  comentarios = 0

  try:
    score_tmp = metadata.find('span', class_='score').text
    score_tmp = score_tmp.replace('points', '').strip()
    score = int(score_tmp)
  except:
    print('No hay score')

  try:  
    #attrs es para buscar por atributos
    comentarios_tmp = metadata.find('span', attrs = {'class' : 'subline'}).text
    comentarios_tmp = comentarios_tmp.split('|')[-1]
    comentarios_tmp = comentarios_tmp.replace('comments', '').strip()
    comentarios = int(comentarios_tmp)
  except:
    print('No hay comentarios')

  print(titulo)
  print(url)
  print(score)
  print(comentarios)
  print()