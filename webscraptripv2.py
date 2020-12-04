import requests
import bs4

'''
#grab page
mainpagetrip = "https://www.tripadvisor.co.uk/"

subpagetrip = "RestaurantSearch-g186338-c10655-oa{}-a_date.2020__2D__12__2D__04-a_people.2-a_time.20%3A00%3A00-a_zur.2020__5F__12__5F__04-p.html#EATERY_LIST_CONTENTS".format(pagenum)

pagegrab = mainpagetrip+subpagetrip
result = requests.get(pagegrab)
soup = bs4.BeautifulSoup(result.text,("lxml"))
soup
'''

def tripchecker():
    mainpagetrip = "https://www.tripadvisor.co.uk/"
    pagenum= 0
    for page in range(1,10):


        subpagetrip = "RestaurantSearch-g186338-c10655-oa{}-a_date.2020__2D__12__2D__04-a_people.2-a_time.20%3A00%3A00-a_zur.2020__5F__12__5F__04-p.html#EATERY_LIST_CONTENTS".format(pagenum)
        pagegrab = mainpagetrip+subpagetrip
        result = requests.get(pagegrab)
        soup = bs4.BeautifulSoup(result.text,("lxml"))
        for item in soup.select("._15_ydu6b"):
            print(item.text)
        pagenum += 30


tripchecker()