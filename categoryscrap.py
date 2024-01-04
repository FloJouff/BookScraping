import requests
from bs4 import BeautifulSoup

import csv

# adresse de la catégorie à scraper:

category_url = "https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html"

page = requests.get(category_url)

if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')

book_urls = []

articles = soup.find_all("article", class_="product_pod")
for article in articles:
    lien = article.find("a")["href"]
    chemin = lien.split("../")
    book_url = "https://books.toscrape.com/catalogue/" + chemin[3]
    book_urls.append(book_url)

print(book_urls[3])


def scrap(url):

    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')

    # Extraction du titre
    titre = soup.find("h1")
    title = titre.string
    print("Titre du livre: " + title)

    # Extraction des données du tableau sous forme de liste
    tds = soup.find_all("td")

    datas = []
    for td in tds:
        datas.append(td.string)

    # Identification des données extraites

    upc = datas[0]
    price_excluding_tax = datas[2]
    price_including_tax = datas[3]
    number_available = datas[5]

    # Nettoyage du nombre d'exemplaire disponible

    available_clean = number_available.strip("In stock ( available)")

    # Extraction de la description du produit

    list_p = soup.find_all("p")

    list_ps = []

    for p in list_p:
        list_ps.append(p.string)

    product_description = str(list_p[3])

    product_description_clean = product_description.strip("</p>")

    # Extraction de la category

    category = soup.find_all("a")

    list_as = []

    for a in category:
        list_as.append(a.string)

    categorie = list_as[3]

    # Extraction de l'adresse de l'image de couverture

    images = []
    for img in soup.find_all('img'):
        images.append(img.get('src'))

    url_image = images[0].replace('../..', 'https://books.toscrape.com/')

    # Extraction de la notation

    note = soup.find("p", class_="star-rating")['class'][1]
    score_value = {
        'One': '1',
        'Two': '2',
        'Three': '3',
        'Four': '4',
        'Five': '5'
    }

    note_finale = score_value[note]

    print("URL de la page produit: " + url)
    print("UPC:" + upc)
    print("Prix HT: " + price_excluding_tax)
    print("Prix TTC: " + price_including_tax)
    print("Nombre d'exemplaires disponibles: " + available_clean)
    print("Description du produit : " + product_description_clean)
    print("Category du livre : " + categorie)
    print("URL de l'image de couverture : " + url_image)
    print("Note du livre : " + note_finale)


for url in book_urls:
    scrap(url)

