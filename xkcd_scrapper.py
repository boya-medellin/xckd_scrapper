import requests
from bs4 import BeautifulSoup as soup
import json
import re

url_main = 'https://xkcd.com/'
headers = {'User-agent' : 'Mozilla/5.0'}
path = '/home/boya/scripts/web_scraping/xkcd/images/'

for i in range(1,3000):
    url = url_main + str(i) + '/'
    req = requests.get(url, headers=headers)
    print("Testing comic #", i , " ...")

    if ( req.ok ):
        print("valid id !")

        # Now to save the image
        html = soup(req.text, 'html.parser')
        img_url = html.find(id='comic')
        img_url = img_url.find('img')
        filename = path + str(i) + str(img_url['title']) + '.png'
        img_url = img_url['src']
        img_url = "https:" + str(img_url)
        
        #Saving bytes to file
        print('saving ...')
        img_req = requests.get(img_url)
        with open (filename, 'wb') as f:
            f.write(img_req.content)

