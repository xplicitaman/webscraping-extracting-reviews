import requests
from bs4 import BeautifulSoup as BS
import html5lib

i=1
j=0
n=int(input("How many reviews do you want? \n"))
while(1):
    if(j==n):
        break
    ua = {"User-Agent":"Chrome"}
    url =f"https://www.amazon.in/20000mAh-Sandstone-Triple-Charging-Delivery/product-reviews/B08HV83HL3/ref=cm_cr_arp_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber={i}"
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