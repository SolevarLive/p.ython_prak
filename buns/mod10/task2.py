import requests
import re

url = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(url)
html = response.text

pattern = r'<h3.*?>(.*?)</h3>'
headings = re.findall(pattern, html)

print(headings)
