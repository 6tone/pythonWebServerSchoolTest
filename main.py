from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import time

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/api/news')
def news():
    res = requests.get('https://tw.yahoo.com/')
    if res.status_code == requests.codes.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        stories = soup.find_all('li', class_='Story-Item')
        data = []        
        for item in stories:
            if item.find('a', class_='story-title') :
                print()
                data.append([item.find('a', class_='story-title').text, item.find('a', class_='story-title').get('href'), item.find('p').text])
        return json.dumps(data)
        
@app.route('/api/hbo')
def hbo():
    my_params = {'date': time.strftime("%Y-%m-%d", time.localtime()), 'channel': 'hbo', 'feed': 'tw'}
    res = requests.get('https://hboasia.com/HBO/zh-tw/ajax/home_schedule', my_params)
    if res.status_code == requests.codes.ok:
        return res.text
        
if __name__ == "__main__":
    app.run(debug=True)