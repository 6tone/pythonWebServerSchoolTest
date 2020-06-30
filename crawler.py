from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import time

my_params = {'date': time.strftime("%Y-%m-%d", time.localtime()), 'channel': 'hbo', 'feed': 'tw'}
res = requests.get('https://hboasia.com/HBO/zh-tw/ajax/home_schedule', my_params)
if res.status_code == requests.codes.ok:
    print(json.dumps(res.text))
    