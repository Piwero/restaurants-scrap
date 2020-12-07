import requests
import bs4
import re
import csv

#change name for link
restaurant_details_class = "wQjYiB7z"

def trip_link_restaurants():
    mainpagetrip = "https://www.tripadvisor.co.uk/"
    pagenum= 0
    restaurant_links= []
    #for page in range(1,10):
    for page in range(1,2):

        subpagetrip = "RestaurantSearch-g186338-c10655-oa{}-a_date.2020__2D__12__2D__04-a_people.2-a_time.20%3A00%3A00-a_zur.2020__5F__12__5F__04-p.html#EATERY_LIST_CONTENTS".format(pagenum)
        pagegrab = mainpagetrip+subpagetrip
        result = requests.get(pagegrab)
        soup = bs4.BeautifulSoup(result.text,("lxml"))
        for item in soup.select("a._15_ydu6b"):
            restaurant_links.append(item['href'])
        pagenum += 30
    return restaurant_links

restaurant_links = trip_link_restaurants()

def trip_restaurant_details():
    mainpagetrip = "https://www.tripadvisor.co.uk/"
    restaurant_name= []
    restaurant_address = []
    restaurant_phone = []

    for link in restaurant_links:
        linkgrab = mainpagetrip + link
        link_result = requests.get(linkgrab)
        soup = bs4.BeautifulSoup(link_result.text,("lxml"))
        #name of restaurant in list
        for name in soup.select("h1._3a1XQ88S"):
            restaurant_name.append(name.text)
    #want to improve this with regular expressions. if phone then add to phone_list, if address to address_list
        #address of restaurant in list
        for detail in soup.select("._2saB_OSe")[0]:
            restaurant_address.append(detail)
        #phone of restaurant in list
        for detail in soup.select("._2saB_OSe")[3]:
            '''Need to add conditional with regular expression of phone pattern
            phone_pattern = re.search'''
            restaurant_phone.append(detail)
    restaurant_dictionary = {i:[j,k] for i,j,k in zip(restaurant_name,restaurant_address,restaurant_phone)}
    return restaurant_dictionary

print(trip_restaurant_details())
#rememeber to change the range in line 13



''''

file_to_output = open("restaurantlinks.csv", "w", newline="")
csv_writer = csv.writer(file_to_output,delimiter=",")

csv_writer.writerows([restaurant_links,])

file_to_output.close()

#go to each link

#scrap info from link and put into list
'''''