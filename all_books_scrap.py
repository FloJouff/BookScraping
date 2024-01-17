from utls import *
import sys


def main():
    print("argv", sys.argv,  len(sys.argv))

    if (len(sys.argv) == 1):
        print("Scrapping de tout le site https://books.toscrape.com/ en cours.")
        get_categories_links()
    else:
        for cat in sys.argv[1:]:
            print("scrapping de ", cat)
            category_scrap(cat)


if __name__ == "__main__":
    main()
