import pdb
import urllib.request
import re
import urllib.parse
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com"

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)

soup = BeautifulSoup(resp, 'lxml')
stuff = soup.find_all('a', attrs={'class':'price'})
with open('cmc.txt', 'w') as f:
    for line in stuff:
        crypto_name = line.attrs['href'].split('/')[2]
        crypto_price = float(line.text.replace("$",""))
        f.write("{:<30s} : {:.2f}\n".format(crypto_name, crypto_price))
