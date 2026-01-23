import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.snapdeal.com/search?keyword=mobile%20phones"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("div", class_="product-tuple-listing")

product_name = []
product_price = []
product_rating = []

for product in products:
    name = product.find("p", class_="product-title")
    product_name.append(name.text.strip() if name else "N/A")

    price = product.find("span", class_="lfloat product-price")
    product_price.append(price.text.strip() if price else "N/A")

    rating = product.find("div", class_="filled-stars")
    product_rating.append(rating["style"] if rating else "No Rating")

df = pd.DataFrame({
    "Product Name": product_name,
    "Price": product_price,
    "Rating": product_rating
})

print("\nSNAPDEAL PRODUCT LIST (MOBILE PHONES)\n")
print(df.to_string(index=False))

df.to_csv("snapdeal_products.csv", index=False)
