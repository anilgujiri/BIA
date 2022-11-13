from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open(r'C:\Anil\Projects\webscraping\housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h1', class_="listing-detail-summary__title").text.replace('\n', '')
        location = list.find('div', class_="listing-detail-summary__location").text.replace('\n', '')
        price = list.find('div', class_="listing-detail-summary__price").text.replace('\n', '')
        area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace('\n', '')
       
        info = [title, location, price, area]
        thewriter.writerow(info)
