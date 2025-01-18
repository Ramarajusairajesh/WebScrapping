import argparse
import sys
import pip
import requests


def scrapper(url):
    result = ""
    response = requests.get(url, timeout=10)
    result = BeautifulSoup(response.content, "html.parser")
    data = result.find_all("p")
    for d in data:
        result = (d.get_text(strip=True))
    print(result)


def install_package():
    try:
        __import__("bs4", "requests", "matplotlib")

    except ImportError:
        pip.main(['install', "bs4" "requests",
                 "matploitlib", "--break-system-packages"])


if __name__ == "__main__":

    install_package()
    from bs4 import BeautifulSoup
    import requests
    parser = argparse.ArgumentParser(
        description="A simple web scrapper written in python3")
    targets = parser.add_mutually_exclusive_group(required=True)
    targets.add_argument("--file", "-f", type=str,
                         help="File containing the URLS")
    targets.add_argument("--url", "-u", type=str,
                         help="Target URL/ URI for scrapping")
    args = parser.parse_args()
    if args.url:
        scrapper(args.url)
    else:
        file = open(args.file, "r")
        for url in file:
            scrapper(url)
