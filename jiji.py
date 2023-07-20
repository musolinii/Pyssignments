import requests
from bs4 import BeautifulSoup
import re
import csv

url = 'https://jiji.co.ke/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div',class_='b-listing-cards__item')

product_list = []


for product in products:
    product_name = product.find('div',class_='b-trending-card__title').text.strip()
    product_price = product.find('div',class_='b-trending-card__price').text.strip()
    product_image = product.find('div',class_='fw-card-media qa-fw-card-media')
    image = product_image.get('style')
    
    image_url = re.search(r"url\(['\"]?(.*?)['\"]?\)", image).group(1)

    product_list.append({'Product name':product_name, 'Product price':product_price, 'image':image_url })


 



with open('jiji.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Product name', 'Product price', 'image'])
    writer.writeheader()
    writer.writerows(product_list)

    




    


