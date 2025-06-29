import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/"
response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, "html.parser")


books = soup.find_all("h3")


for book in books:
    print(book.a["title"])
