import requests
from bs4 import BeautifulSoup

WEBSITE ="https://www.khanacademy.org"
resp = requests.get(WEBSITE)
contents = resp.text

bs = BeautifulSoup(contents, "html.parser")
links = bs.find_all("a")
for link in links:
    href = link['href']
    if href == 'javascript:void(0)':
        continue

    if href.startswith("http"):
         print(href)
    else:
         print(WEBSITE + href)




