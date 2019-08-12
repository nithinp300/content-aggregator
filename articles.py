from bs4 import BeautifulSoup
import requests

url = "https://techcrunch.com/"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

h2_tags = content.findAll('h2')
h3_tags = content.findAll('h3')
h2_tags_text = []
for h2 in h2_tags:
	h2_tags_text.append(h2.get_text().strip())

# method to get A tags from header tags (h1, h2, h3...)
def get_a_tags(a_tags, h_tags):
	for h in h_tags:
	    if not h.a is None:
	        a_tags.append(h.a)

a_tags = []
get_a_tags(a_tags, h2_tags)
get_a_tags(a_tags, h3_tags)

articles = []
for a in a_tags:
	headline = a.get_text().strip()
	link = a.get('href')
	if url in link:
		articles.append(a)
	#print(a.get('href'))
for a in articles:
	print(a.get_text().strip())
	#print(a.get('href'))
