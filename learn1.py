
from urllib.request import urlopen

html = urlopen('https://jr.jd.com')
print(html.read())
html.close()