import requests
from bs4 import BeautifulSoup
import csv

def get_soup(url, headers):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, "html.parser")

def extract_product_data(soup):
    products = []
    count = 0
    for item in soup.find_all("div", class_="thumbnail"):
        if count >= 10:
            break
        name = item.find("a", class_="title")
        price = item.find("h4", class_="price")
        rating = item.find("p", class_="pull-right")

        name_text = name.get_text(strip=True) if name else "N/A"
        price_text = price.get_text(strip=True) if price else "N/A"
        rating_text = rating.get_text(strip=True) if rating else "N/A"

        products.append([name_text, price_text, rating_text])
        count += 1
    return products

def save_to_csv(products, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Rating"])
        writer.writerows(products)

def scrape_products(url, output_file):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    soup = get_soup(url, headers)
    products = extract_product_data(soup)
    save_to_csv(products, output_file)
    print(f"Data saved to {output_file}")

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
output_file = "products.csv"
scrape_products(url, output_file)
