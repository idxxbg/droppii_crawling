import requests
from bs4 import BeautifulSoup

# details_url = "https://droppii.vn/san-pham/combo-2-chai-ngoc-linh-truong-sinh-gold/"
# response = requests.get(details_url)

# if response.status_code == 200 :
#     soup = BeautifulSoup(response.text, 'html.parser')
#  # Những thành phần chi tiết lấy thêm 
#     product_description = soup.select_one('.summary > .description > p'  )
#     product_content = soup.select('.resp-tabs-container > .tab-content'  )
#     product_image_thumbnail = soup.select('.img-thumbnail > img.img-responsive')
#     product_category = soup.select('.breadcrumb li[itemprop="itemListElement"]')[1:]
    
#     # Lấy phần text của từng thẻ <p> và lưu vào danh sách
#     if product_description:
#         description_ = product_description
#     else:
#         description_ = []

#     if product_content:
#         content_ = [p.text.strip().replace("\xa0", " ") for p in product_content]
#     else:
#         content_ = []

#     if product_image_thumbnail:
#         thumbnail_urls = [
#             img['src'] for img in product_image_thumbnail if img.get('src')
#         ]
#     else:
#         thumbnail_urls = []
 
#     if product_category :
#         category = [p.text.strip() for p in product_category if p]
#     else:
#         category = []
# print(category)


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
        content_ = [p.text.strip().replace("\xa0", " ") for p in product_content]
    else:
        content_ = []

    # lấy hình ảnh thumbnail
    product_image_thumbnail = soup.select('.img-thumbnail > img.img-responsive')
    if product_image_thumbnail:
        thumbnail_urls = [img['src'] for img in product_image_thumbnail if img.get('src')]
    else:
        thumbnail_urls = []

    return {
        "description": description_,
        "content" : content_,
        'thumbnail_urls' : thumbnail_urls,
    }

