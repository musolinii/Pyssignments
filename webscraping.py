import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div',class_='css-xdandi')
data = []

for article in articles[:10]:
    title = article.find('h3').text.strip()
    # description = article.find('p').text.strip()
    # data.append({'title': title, 'description': description})
    data.append({'title':title})
    
    

with open('nytimes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)

print("Data has been scraped and stored in 'nytimes.csv' file.")
