import requests
from bs4 import BeautifulSoup as BS
import html5lib

i=1
j=0
n=int(input("How many reviews do you want to print? \n"))
while(1):
    if(j==n):
        break
    ua = {"User-Agent":"Chrome"}
    url =f"https://www.flipkart.com/nothing-phone-1-black-128-gb/product-reviews/itmeea53a564de47?pid=MOBGCYGPFEGDMYQR&lid=LSTMOBGCYGPFEGDMYQRIMJJ0P&marketplace=FLIPKART&page={i}"
    page = requests.get(url, headers=ua)
    soup = BS(page.content, "html5lib")

    names=soup.find_all("p", class_="_2sc7ZR _2V5EHH")
    reviews=soup.find_all("div", class_="t-ZTKy")
    if(reviews==None):
        break

    for name,review in zip(names,reviews):
        name=name.text.strip()
        review=review.find("div")
        unwanted=review.find("span")
        unwanted.extract()

        if(review==None):
            j+=1
            print(j)
            continue

        review=review.text.strip()
        
        print(f"{j+1}. {name}: {review}\n")
        j+=1
        if(j==n):
            break
    i+=1