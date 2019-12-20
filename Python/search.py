#!/usr/bin/python
#WebScraping

import urllib.request

with urllib.request.urlopen('https://tel.search.ch/?was=Berufsschule&wo=Muttenz') as htmlpage:
    content = htmlpage.read()

len(content),content[:100]

import re

re.findall(r'0\d{2} d{3} \d{2} \d{2}',content.decode())
