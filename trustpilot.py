import requests
from bs4 import BeautifulSoup as BS
import html5lib

website = input("Enter the website you want reviews for: ")

url = f"https://www.trustpilot.com/review/{website}"
page = requests.get(url)

soup = BS(page.content, "html5lib")

# Extracting name of website, overall rating, reviews, name of reviewers, location of reviewers, and star rating (posted by them) of the website being searched for:
name = soup.find("span", class_="typography_display-s__qOjh6")
rating = soup.find("p", class_="typography_body-l__KUYFJ")
reviews = soup.find_all("p", class_="typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn", limit=3)
reviewers = soup.find_all("span", class_="typography_heading-xxs__QKBS8 typography_appearance-default__AAY17", limit=3)
locations = soup.find_all("div", class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_detailsIcon__Fo_ua", limit=3)
stars = soup.find_all("div", class_="styles_reviewHeader__iU9Px", limit=3)


# Extracting text from the variables that store BS element:
name = name.text.strip()
rating = rating.text.strip()

# Printing website rating and its link:
print(f"{name}: {rating} --> {website}\n")

for i,(reviewer,review,location,star) in enumerate(zip(reviewers,reviews,locations,stars), start=1):
    reviewer = reviewer.text.strip()
    review = review.text.strip()
    location = location.text.strip()
    star=star["data-service-review-rating"]
    
    print(f"{i}. Posted by {name} from {location} - Rating: {star} out of 5 -\n{review}\n")

