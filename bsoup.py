import urllib.request
import pdb
from bs4 import BeautifulSoup

quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = urllib.request.Request(quote_page)
resp = urllib.request.urlopen(page)
soup = BeautifulSoup(resp, 'html.parser')

name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print(name)
price_box = soup.find('div', attrs={'class':'price'})
price=price_box.text
print(price)
pdb.set_trace()
#name = name_box.text.strip()
#print(name)
