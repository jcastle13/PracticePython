import requests
import string
from bs4 import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

#print("r_html:", r_html)

soup = BeautifulSoup(r_html, "lxml")
#BeautifulSoup(r_html)
title = soup.find('article') #, 'article')


print("title:", title)

