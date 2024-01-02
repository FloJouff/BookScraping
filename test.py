import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/catalogue/saga-volume-6-saga-collected-editions-6_924/index.html"

response = requests.get(url)

html = response.content

soup = BeautifulSoup(html, 'html.parser')


notations = soup.find_all("p", class_="star-rating")

print(notations[0])
