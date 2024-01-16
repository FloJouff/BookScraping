from utls import *
import sys


def main():
    print("argv ", sys.argv,  len(sys.argv))

    if (len(sys.argv) == 1):
        print(" scrapping de tout site en cours https://books.toscrape.com/")
        get_categories_links()
    else:
        for cat in sys.argv[1:]:
            print("scrapping de ", cat)
            category_scrap(cat)


if __name__ == "__main__":
    main()
