import requests
from bs4 import BeautifulSoup

details_url = "https://droppii.vn/san-pham/thuc-pham-bao-ve-suc-khoe-cnd-ginseng-nhan-sam-hoat-huyet/"
response = requests.get(details_url)

if response.status_code == 200 :
    soup = BeautifulSoup(response.text, 'html.parser')
 # Những thành phần chi tiết lấy thêm 
    product_content = soup.select_one('.summary > .description > p'  ),
    product_description = soup.select_one('.resp-tabs-container > .tab-content'  )
    # Lấy phần text của từng thẻ <p> và lưu vào danh sách
    if product_content:
        content_ = [p.text.strip() for p in product_description]
    else:
        content_ = []

    if product_description:
        description_ = [p.text.strip().replace("\xa0", " ") for p in product_description]
    else:
        description_ = []
 
# print( content_,description_ )

# xử lý thông tin chi tiết trong từng sản phẩm 
 # Hàm lấy thông tin chi tiết   
def get_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

   # Lấy phần tử mô tả sản phẩm
    product_description = soup.select_one('.summary > .description > p')
    if product_description:
        description_ = [product_description.text.strip().replace("\xa0", " ")]
    else:
        description_ = []

     # Lấy nội dung chi tiết sản phẩm
    product_content = soup.select_one('.resp-tabs-container > .tab-content')
    if product_content:
        content_ = [p.text.strip().replace("\xa0", " ") for p in product_content.find_all('p')]
    else:
        content_ = []

    return {
        "description": description_,
        "content" : content_
    }

