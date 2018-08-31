import pdb
import urllib.request
import re
import urllib.parse
from bs4 import BeautifulSoup
import datetime

#url = "https://coinmarketcap.com"
#url = "https://scholar.google.com/citations?user=ikdrOCMAAAAJ&hl=en"
url = "https://scholar.google.com/citations?hl=en&user=ikdrOCMAAAAJ&view_op=list_works&sortby=pubdate"
headers={}
#headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

req = urllib.request.Request(url,headers=headers)
resp = urllib.request.urlopen(req)

soup = BeautifulSoup(resp, 'lxml')
stuff = soup.find_all('td', attrs={'class':'gsc_a_t'})
with open("bib.txt", 'a') as f:
    f.write('========Updated {}=====\n'.format(datetime.datetime.now()))
    for line in stuff:
        items = [thing for thing in line.strings]
        title = items[0]
        authors = items[1]
        publication_info = items[2]
        year = items[3].replace(",","").strip()
        f.write("{}\n{}\n{}\n{}\n".format(title, authors, publication_info, year))
        f.write("*"*20)
        f.write("\n")
    f.write('========End {}=======\n'.format(datetime.datetime.now()))


