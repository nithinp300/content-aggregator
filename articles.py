from bs4 import BeautifulSoup
import requests

url = "https://thenextweb.com/"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

h2_tags = content.findAll('h')
h2_tags_text = []
for h2 in h2_tags:
	h2_tags_text.append(h2.get_text().strip())

a_tags = []
for h2 in h2_tags:
    if not h2.a is None:
        a_tags.append(h2.a)
for a in a_tags:
	print(a.get_text())
	#print(a.get('href'))
