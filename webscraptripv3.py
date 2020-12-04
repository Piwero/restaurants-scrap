import requests
import bs4
import csv

def tripchecker():
    mainpagetrip = "https://www.tripadvisor.co.uk/"
    pagenum= 0
    restaurantlist= []
    for page in range(1,10):


        subpagetrip = "RestaurantSearch-g186338-c10655-oa{}-a_date.2020__2D__12__2D__04-a_people.2-a_time.20%3A00%3A00-a_zur.2020__5F__12__5F__04-p.html#EATERY_LIST_CONTENTS".format(pagenum)
        pagegrab = mainpagetrip+subpagetrip
        result = requests.get(pagegrab)
        soup = bs4.BeautifulSoup(result.text,("lxml"))
        for item in soup.select("._15_ydu6b"):
            restaurantlist.append(item.text)
        pagenum += 30
    return restaurantlist

restaurant_names = tripchecker()


file_to_output = open("restaurantlisttrip.csv", "w", newline="")
csv_writer = csv.writer(file_to_output,delimiter=",")

csv_writer.writerows([restaurant_names,])

file_to_output.close()

