import requests
import csv
from bs4 import BeautifulSoup

# set the URL for the search query
search_query = "iphone"

url = "https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_query}"

# send a GET request to the URL and store the response
response = requests.get(url)

# create a BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, "html.parser")

# find all product listings on the page
product_listings = soup.find_all("div", class_="organic-listing")

# create a CSV file to write the product data to
with open(f"{search_query}.csv", mode="w", encoding="utf-8", newline="") as csv_file:
    # create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # write the header row to the CSV file
    csv_writer.writerow(["Product Name", "Price", "Min Order Quantity", "Supplier"])

    # loop through each product listing and extract the relevant data
    for product in product_listings:
        # get the product name
        product_name = product.find("h2").text.strip()

        # get the price
        price = product.find("div", class_="price").text.strip()

        # get the minimum order quantity
        min_order_quantity = product.find("div", class_="min-order").text.strip()

        # get the supplier name
        supplier = product.find("div", class_="company").find("a").text.strip()

        # write the data to the CSV file
        csv_writer.writerow([product_name, price, min_order_quantity, supplier])