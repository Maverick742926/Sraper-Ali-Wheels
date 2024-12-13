import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.alibaba.com/product-detail/Motorcycle-Gear-shift-switch-display-cable_1600620653543.html?spm=a2700.galleryofferlist.0.0.7094cbeefiW4OZ'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Create a CSV file
csv_file = open('alibaba_products.csv', 'w', newline='')
writer = csv.writer(csv_file)

# Write headers to CSV file
writer.writerow(['Product Name', 'Price', 'Minimum Order Quantity', 'Product Link'])

# Loop through 5 pages of products
for page in range(1, 6):
    page_url = url.format(page)
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all product listings on the page
    product_listings = soup.find_all('div', class_='organic-listing')

    # Loop through each product listing and extract the product information
    for product in product_listings:
        product_name = product.find('h2', class_='title').text.strip()
        product_price = product.find('div', class_='price').text.strip()
        min_order_qty = product.find('div', class_='min-order').text.strip()
        product_link = product.find('a', class_='organic-img').get('href')

        # Write the product information to the CSV file
        writer.writerow([product_name, product_price, min_order_qty, product_link])

# Close the CSV file
csv_file.close()