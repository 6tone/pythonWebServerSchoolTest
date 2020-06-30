import requests
from bs4 import BeautifulSoup
import json


res = requests.get('https://tw.yahoo.com/')
if res.status_code == requests.codes.ok:
  soup = BeautifulSoup(res.text, 'html.parser')
  stories = soup.find_all('a', class_='story-title')
  data = []
  for item in stories:
    data.append(json.dumps([item.text, item.get('href')])

  print(json.loads(data))



