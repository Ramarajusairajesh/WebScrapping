
import argparse
import requests
from bs4 import BeautifulSoup
from time import sleep

file = open("prices.txt", "a")


def prize_comparision(url):
   headers = {
'authority': 'www.amazon.com',
'pragma': 'no-cache',
'cache-control': 'no-cache',
'dnt': '1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-dest': 'document',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.find('span', attrs={"class": "a-price-whole"})
        product_name = soup.find('span', attrs={"class": "a-profile-name"})
        if price_element:
            price = price_element.get_text(strip=True)
            data = f"{product_name.get_text(strip=True)}: {price}"
            file.write(data)
        else:
            print("Price element not found. Please check the product URL.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}\nDetails: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Price comparison tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", type=str,
                       help="Product URL", dest="product")
    group.add_argument("-f", "--file", type=str,
                       help="File containing product URLs", dest="file")
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r") as file1:
                for line in file1:
                    url = line.strip()
                    if url:
                        prize_comparision(url)
                        # Add delay between requests to avoid triggering rate-limiting
                        sleep(86400)
        except FileNotFoundError:
            print(f"File not found: {args.file}")
    else:
        while True:
            prize_comparision(args.product)
            sleep(86400)
