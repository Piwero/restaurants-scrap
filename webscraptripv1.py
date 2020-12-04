import requests
import bs4


#grab page
mainpagetrip = "https://www.tripadvisor.co.uk/"
subpagetrip = "Restaurants-g186338-c36-London_England.html"
pagegrab = mainpagetrip+subpagetrip
result = requests.get(pagegrab)

soup = bs4.BeautifulSoup(result.text,("lxml"))
soup


print(soup.select("._15_ydu6b"))

for item in soup.select("._15_ydu6b"):
    print(item.text)