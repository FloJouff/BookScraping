import requests
from bs4 import BeautifulSoup

import csv

# adresse du livre à scraper:

url = "https://books.toscrape.com/catalogue/carrie_671/index.html"

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

# Préparation du fichier CSV

en_tete = ["URL", "Titre", "UPC", "Prix HT", "Prix TTC", "disponibilité",
           "Category", "Description", "URL de l'image de couverture",
           "Notation"]
ligne1 = [url, title, upc, price_excluding_tax, price_including_tax,
          available_clean, categorie, product_description_clean, url_image,
          note_finale]

# Création du fichier CSV

with open('data.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    writer.writerow(ligne1)
