import urllib
import urllib.request
from bs4 import BeautifulSoup
import random

for i in range(1,20,1):
    theurl = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_1&otracker1=AS_QueryStore_OrganicAutoSuggest_0_1&as-pos=0&as-type=HISTORY&page="+str(i)
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    values = soup.find_all("div",{"class": "bhgxx2 col-12-12"})
    for value in values:
        brand_name = value.findAll("div", {"class": "_3wU53n"})
        link = value.findAll("a",{"class": "_31qSD5"})
        price = value.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
        discount = value.findAll("div", {"class": "VGWI6T"})
        rating = value.findAll("div", {"class": "hGSR34"})
        imag = value.findAll("img", {"class": "_1Nyybr  _30XEf0"})

        link_foor = []
        brand_names = []
        specs = []
        prices = []
        discounts = []
        linkofimg = []

        for b in brand_name:
            brand_names.append(b.text)
    #for c in brand:
     #   specs.append(c.text)
        for d in price:
            prices.append(d.text)
        for c in discount:
            discounts.append(c.text)
        for v in link:
            z = (v.get("href"))
            if z[:1] == "/":
                z = "https://flipkart.com" + z;
            link_foor.append(z + "/n")
        for f in rating:
            linkofimg.append(f.text)


        for b in brand_names:
            print(b)
        for d in prices:
            print(d)
        for c in discounts:
            print(c)
        for v in link_foor:
            print(v)
        for f in linkofimg:
            print(f)


