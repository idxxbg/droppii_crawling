import requests
import json
from bs4 import BeautifulSoup

from details import get_product_details

products = []

# URL cơ bản của shop
base_url = 'https://droppii.vn/shop/page/'

# Lặp qua từng trang từ 1 đến 145
for page in range(1, 146):  # 1 -> 145
    print(f"Đang xử lý trang {page}...")
    url = f"{base_url}{page}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Lấy dữ liệu từ trang hiện tại
        links = soup.select('.archive-products > .products > .product-col > .product-inner > .product-image > a')
        product_image = soup.select('.archive-products > .products > .product-col > .product-inner > .product-image > a > .inner > img')
        product_onSale = soup.select('.archive-products > .products > .product-col > .product-inner > .product-image > a > .labels > .onSale')
        product_titles = soup.select('.archive-products > .products > .product-col > .product-inner > .product-content > a > h3')
        product_price = soup.select('.archive-products > .products > .product-col > .product-inner > .product-content > .price > .woocommerce-Price-amount > bdi')

        # Tạo danh sách sản phẩm từ trang hiện tại
        for i in range(len(links)):
            try:
                onSale = product_onSale[i].text.strip() if i < len(product_onSale) else None
                product = {
                    'link': links[i]['href'],
                    'image_src': product_image[i]['src'],
                    'onSale': onSale,
                    'title': product_titles[i].text.strip(),
                    'price': product_price[i].text.strip(),
                }
                products.append(product)
            except IndexError:
                pass

    else:
        print(f"Không thể truy cập trang {page}. Mã lỗi: {response.status_code}")

# Lấy thông tin chi tiết sản phẩm
for product in products:
    details = get_product_details(product["link"])
    product.update(details)

# Xuất dữ liệu ra file JSON
with open('products.json', 'w', encoding='utf-8') as json_file:
    json.dump(products, json_file, ensure_ascii=False, indent=3)

print("Dữ liệu đã được xuất ra file products.json.")

