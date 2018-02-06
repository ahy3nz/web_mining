import pdb
import BeautifulSoup
import urllib.request
import re
import urllib.parse
#response = urllib.request.urlopen('http://www.google.com/')
#html = response.read()

#url = 'https://www.google.com/search'
#url = 'https://www.yahoo.com/search'
#values = {'q': 'python programming tutorials'}
#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
#req = urllib.request.Request(url, data)
#resp = urllib.request.urlopen(req)
#respData=resp.read()
#print(respData)
#pdb.set_trace()

#--------------------#
#try:
#    url = 'https://www.google.com/search?q=python'
#    headers  = {}
#    # To show we're not a bot
#    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
#
#    # Construct the request
#    req = urllib.request.Request(url, headers = headers)
#
#    # Make the request, get response
#    resp =  urllib.request.urlopen(req)
#
#    # Actually read the response
#    respData = resp.read()
#
#    # SAve
#    saveFile=open('noheaders.txt', 'w')
#    saveFile.write(str(respData))
#    saveFile.close()
#except Exception as e:
#    print(str(e))

#-----------------#
url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
for eachP in paragraphs:
    print(eachP)
