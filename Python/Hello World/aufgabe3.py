import urllib.request
import re

sock=urllib.request.urlopen("http://python.org")

page=sock.read().decode('utf-8')
links = re.findall(r'<link.*?>',page)
sock.close()

print(links)