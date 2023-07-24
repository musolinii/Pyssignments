import requests
from bs4 import BeautifulSoup
import re
import csv

url = 'https://www.jumia.co.ke/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

section_things = soup.find_all('section',class_='card -oh _fw -rad4')

product_list = []

for thing in section_things:

    section_name = thing.find('h2',class_='-m -fs20 -elli').text.strip()
    if section_name == "This Week's Top Deals | Deals up to 40% Off":

        products = thing.find_all('div',class_='itm col')

        for product in products:
            product_name = product.find('div',class_='name').text.strip()
            product_price = product.find('div',class_='prc').text.strip()

            try:
                discount = product.find('div',class_='bdg _dsct').text.strip()
            except:
                discount = "0%"

            product_list.append({'Product name':product_name, 'Product price':product_price, 'discount':discount })



with open('jumia.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Product name', 'Product price', 'Discount'])
    writer.writeheader()
    writer.writerows(product_list)

       
