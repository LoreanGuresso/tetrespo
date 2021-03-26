# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter link')
count = input('Enter count')
position = input('Enter position')

try:
    count = int(count)

except:
    print("ingresar un número")

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
tags = soup('tr')
for tag in tags:
    # Look at the parts of a tag

    #print('URL:', tag.get('tr', None))
    #print('Contents:', tag.contents[1])


    com = str(tag)
    number = re.findall("[0-9.]+" ,com)
    #print(number)

    for num in number:
        if len(num)>0:
            entero = int(num)
            total = total + entero
            print(total)
