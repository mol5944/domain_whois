import requests
from bs4 import BeautifulSoup

domain = input('domain: ')
resp = requests.get('https://www.nic.ru/whois/?searchWord=' + domain)
soup = BeautifulSoup(resp.text,'html.parser')

print('########################################')
for i in soup.find_all('li',class_="_2ag2R"):
    print(i.find_all('span')[0].get_text().strip() + ' ' + i.find_all('span')[1].get_text().strip())
print('########################################')
