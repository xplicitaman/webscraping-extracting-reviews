import requests
from bs4 import BeautifulSoup as BS
import html5lib

# Code to get a list of products using keyword:

keyword=input("Enter the product you want to search on Amazon: ")
url=f"https://www.amazon.in/s?k={keyword}"

page=requests.get(url)

soup=BS(page.content, "html5lib")

names=soup.find_all("span", class_="a-size-medium a-color-base a-text-normal", limit=10)
links=soup.find_all("div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16", limit=10)

logos=[]
for image in links:
    image=image.find("img")
    image=image["src"]
    logos.append(image)

prodcodes=[]
for i,(name,link,logo) in enumerate(zip(names,links,logos), start=1):
    name=name.text.strip()
    link=link["data-asin"]
    print(f"{i}. {name} -> Logo: {logo} \nLink: amazon.in/dp/{link}\n")
    prodcodes.append(link)


# Code to get reviews of chosen product:
i=1
j=0
sr=int(input("Which product do you want to explore? (type sr. no)\n"))
n=int(input("How many reviews do you want? \n"))
while(1):
    if(j==n):
        break
    ua = {"User-Agent":"Chrome"}
    url=f"https://www.amazon.in/product-reviews/{prodcodes[sr-1]}/ref=cm_cr_arp_d_paging?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"
    page = requests.get(url, headers=ua)
    soup = BS(page.content, "html5lib")

    names=soup.find_all("div",class_="a-section celwidget")
    reviews=soup.find_all("span", class_="a-size-base review-text review-text-content")
    ratings=soup.find_all("i", {"data-hook":"review-star-rating"})

    if(reviews==None):
       break

    for name,review,rating in zip(names,reviews,ratings):
        name=name.find("span", class_="a-profile-name")
        name=name.text.strip()

        rating=rating.find("span")
        rating=rating.text.strip().split()
        rating=rating[0]

        review=review.find("span")
        if(review==None):
            print(f"{j+1}. {name}: (rating: {rating}) - <img>\n")
            j+=1
            continue
        review=review.text.strip()

        
        print(f"{j+1}. {name}: (rating: {rating}) \n {review}\n")
        j+=1
        if(j==n):
            break
    i+=1