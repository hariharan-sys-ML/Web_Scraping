import requests
from bs4 import BeautifulSoup
import pandas as pd

book_list = []
for page in range(0, 51):
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for i in books:
        title = i.find("h3").find("a")["title"]
        Rating = i.find("p", class_="star-rating")["class"][1]
        price = i.find("p", class_="price_color").text.strip()

        book_list2 = [title, Rating , price]
        book_list.append(book_list2)

df = pd.DataFrame(book_list, columns=["Title", "Rating", "Price"])
df.to_csv("books.csv", index=False)



