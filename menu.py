from utls import *


def main(): 

    while True:
        print("1. pour scrapper tout le site https://books.toscrape.com/ ")
        print("2. pour scrapper une categorie ")
        print("3. pour scrapper un book ")
        print("0. pour quitter  ")
        menu_choix = input("faites votre choix: ")
        if menu_choix == "1":
            get_categories_links()
        elif menu_choix == "2":
            cat = input("lien de la categorie: ")
            category_scrap(cat)
        elif menu_choix == "3":
            book = input("lien du book: ")
            book_scrap(book)
        elif menu_choix == "0":
            break
        else:
            print("bad choose")


if __name__ == "__main__":
    main()
