
from urllib.request import urlopen

html =  urlopen('httpL//jr.jd.com')
print(html.read())
html.close()