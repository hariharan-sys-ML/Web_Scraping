import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

book = soup.find("article", class_="product_pod")

title = book.find("h3").find("a")["title"]
Rating = book.find("p", class_="star-rating")["class"][1]
price = book.find("p", class_="price_color").text.strip()

print("Book title:", title)
print("Price:", price)
print("Rating:", Rating)
