import requests
from bs4 import BeautifulSoup
from re import search

print('########################################')

domain = input('domain: ')
resp = requests.get('https://www.nic.ru/whois/?searchWord=' + domain)

soup = BeautifulSoup(resp.text,'html.parser')

try:
    for i in soup.find('div',class_="_3U-mA _23Irb").get_text().split('\r\n\r\n')[0].split('\r\n'):
        print(i.strip())
except:
    pass

try:
    for i in soup.find_all('li',class_="_2ag2R"):
        print(i.find_all('span')[0].get_text().strip() + ' ' + i.find_all('span')[1].get_text().strip())
except:
    pass

print('########################################')
