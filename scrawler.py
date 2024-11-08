import requests
import json
from bs4 import BeautifulSoup

from details import get_product_details


products = []

# lấy dữ liệu từ trang sản phẩm 

shop_url = 'https://droppii.vn/shop/'
response = requests.get(shop_url)


if(response.status_code == 200):
    soup = BeautifulSoup(response.content, 'html.parser')

# các trường dữ liệu trong trang sản phẩm đã lấy
links = soup.select('.product-col > .product-inner > .product-image > a ')
product_image = soup.select('.product-col > .product-inner > .product-image > a > .inner > img ')
product_label = soup.select('.product-col > .product-inner > .product-image > a > .labels > .onhot ')
product_titles = soup.select('.product-col > .product-inner > .product-content > a > h3 ')
product_rating = soup.select('.product-col > .product-inner > .product-content > .rating-wrap > .rating-content > .star-rating   ')
product_price = soup.select('.product-col > .product-inner > .product-content > .price > .woocommerce-Price-amount > bdi  ')

# tạo file Json dữ liệu của product
for i in range(len(links)) :
    try:
        label = product_label[i].text.strip() if i < len(product_label) else None
        product = {
            
            'link' : links[i]['href'],
            'image_src' : product_image[i]['src'],
            'label' : label,
            'title' : product_titles[i].text.strip(),
            'price' : product_price[i].text.strip(),
        }
        products.append(product)
    except IndexError:
        pass


for product in products:
    details = get_product_details(product["link"])
    product.update(details)

# json transform 
# Xuất dữ liệu ra file JSON
with open('products.json', 'w', encoding='utf-8') as json_file:
    json.dump(products, json_file, ensure_ascii=False, indent=3)

print("Dữ liệu đã được xuất ra file products.json.")

