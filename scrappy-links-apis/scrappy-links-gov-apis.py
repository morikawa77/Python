import requests
from bs4 import BeautifulSoup
import pandas as pd
 
urls = 'https://www.gov.br/conecta/catalogo/'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
 
data = []

for link in soup.find_all("a"):
   text, url = ''

   if link.get('href') is not None:
      url = link.get('href')
   elif link.find('a') is not None:
      text = link.find('a')

   data.append([text, url])

df = pd.DataFrame(data[24:], columns=['Titles', 'URLs'])
df.to_excel(excel_writer = "links.xlsx", index=False)