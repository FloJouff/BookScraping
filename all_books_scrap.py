import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
import os.path


""" fonction permettant de récupérer les données de chaque livres """


def book_scrap(url):

    book_page = requests.get(url)

    soup = BeautifulSoup(book_page.content, 'html.parser')

    # Extraction du titre
    titre = soup.find("h1")
    title = titre.string
    title = title.replace(':', '_')
    title = title.replace('/', '_')
    title = title.replace('\\', '_')
    title = title.replace('\'', '_')
    title = title.replace('\"', '_')
    title = title.replace('*', '_')
    title = title.replace('~', '_')
    title = title.replace('`', '_')
    title = title.replace('?', '_')

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

    # Gestion des cas particuliers:

    exclu = "star-rating"
    if exclu in product_description:
        product_description_clean = "Pas de description disponible"
    else:
        product_description_clean = product_description.strip("</p>")

    # Extraction de la categorie

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

    book_data = (
            {'title': title,
            'url': url,
            'UPC': upc,
            'PRIX HT': price_excluding_tax,
            'PRIX TTC': price_including_tax,
            'disponibilité': available_clean,
            'Description du produit': product_description_clean,
            'Categorie': categorie,
            'URL de l\'image de couverture': url_image,
            'Note': note_finale}
        )

    add_data_to_csv(categorie, book_data)

    # Création du fichier image:

    os.makedirs('images' + '//' + f'{categorie}', exist_ok=True)
    f = open('images' + '//' + f'{categorie}' + '//' + f'{title}.jpg', "wb")
    f.write(urllib.request.urlopen(url_image).read())
    f.close()


""" Fonction permettant de scraper tous les livres d'une catégorie"""


def category_scrap(categorie_url):
    # adresse de la catégorie à scraper:
    book_urls = []

    page = requests.get(categorie_url)

    if page.status_code == 200:
        cat_soup = BeautifulSoup(page.content, 'html.parser')     

    articles = cat_soup.find_all("article", class_="product_pod")
    for article in articles:
        lien = article.find("a")["href"]
        chemin = lien.split("../")

        book_url = "https://books.toscrape.com/catalogue/" + chemin[2]

        book_urls.append(book_url)

    for url in book_urls:
        book_scrap(url)

    base_url = str(categorie_url).split('index.html')
    next_element = cat_soup.find("li", class_="next")

    while next_element is not None:

        next_index_page = next_element.find("a", href=True)["href"]
        link = requests.get(str(base_url[0]) + next_index_page)

        soup = BeautifulSoup(link.text, 'html.parser')
        book_urls = []

        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            lien = article.find("a")["href"]
            chemin = lien.split("../")
            book_url = "https://books.toscrape.com/catalogue/" + chemin[2]
            book_urls.append(book_url)

        for url in book_urls:
            book_scrap(url)

            next_element = soup.find("li", class_="next")


"""
fonction permettant de récuperer les urls de toutes les catégories,
à partir de la page d'accueil"""


def get_categories_links():

    main_url = "https://books.toscrape.com/index.html"
    main_page = requests.get(main_url)

    if main_page.status_code == 200:
        soup = BeautifulSoup(main_page.content, 'html.parser')

    cats = soup.find("ul", class_="nav nav-list")

    links = cats.find_all("a")
    categories_url = []

    for link in links:
        categories_url.append(("https://books.toscrape.com/" + link["href"]))

    for categorie in categories_url:
        category_scrap(categorie)


"""   fonction permettant la Création du fichier CSV   """


def add_data_to_csv(categorie_name, book_data):
    if os.path.isfile('fichiers_csv' + '//' + f'{categorie_name}.csv'):
        with open('fichiers_csv' + '//' + f'{categorie_name}.csv', 'a',
                  encoding='UTF-8-sig') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=",")
            writer.writerow(book_data.values())
    else:
        en_tete = ["Titre", "URL", "UPC", "Prix HT", "Prix TTC",
                   "disponibilité", "Description", "Categorie",
                    "URL de l'image de couverture", "Notation"]

        with open('fichiers_csv' + '//' + f'{categorie_name}.csv', 'a',
                  encoding='UTF-8-sig') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=",")
            writer.writerow(en_tete)
            writer.writerow(book_data.values())


def main():
    get_categories_links()


if __name__ == "__main__":
    main()
