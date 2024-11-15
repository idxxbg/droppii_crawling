import requests

# push code

api_url = "https://droppii.live/wp-json/wc/v3/products"
consumer_key = 'ck_9cb11b1ad23303a2352a3db87bffca3523832527'
consumer_secret = 'cs_50668383e8bbf9f4ccc6c849e66b30a6e0e110b0'

# Tạo sản phẩm mới
product_data = {
    "link": "https://droppii.vn/san-pham/thuc-pham-bao-ve-suc-khoe-cnd-ginseng-nhan-sam-hoat-huyet/",
      "image_src": "https://droppii.vn/wp-content/uploads/2024/04/NHAN-SAM-HOAT-HUYET-3-1.jpg?x99204",
      "label": "Hot",
      "title": "Thực phẩm bảo vệ sức khỏe CND Ginseng nhân sâm hoạt huyết (kèm túi)",
      "price": "490,000 ₫",
      "description": [],
      "content": [
         "1. Tên sản phẩm: Thực phẩm bảo vệ sức khỏe CND GINSENG nhân sâm hoạt huyết",
         "2. Thương hiệu: CND GINSENG",
         "3. Xuất xứ: Việt Nam",
         "4. Thành phần:",
         "5. Công dụng:",
         "6. Đối tượng sử dụng:",
         "7. Cách dùng:",
         "8. Quy cách đóng gói: 20 gói/ hộp",
         "9. Thời hạn sử dụng sản phẩm: 36 tháng kể từ ngày sản xuất. Ngày sản xuất và hạn sử dụng được ghi trên nhãn chính của sản phẩm.",
         "10. Bảo quản: ở nơi khô ráo và thoáng mát, tránh ánh nắng chiếu trực tiếp.",
         "11. Chú ý:",
         "Sản xuất tại:",
         "Chịu trách nhiệm và phân phối sản phẩm:"
      ]
   },
# Gửi yêu cầu POST để tạo sản phẩm
response = requests.post(api_url, json=product_data, auth=(consumer_key, consumer_secret))

# Kiểm tra phản hồi
if response.status_code == 201:
    print("Sản phẩm đã được tạo thành công:", response.json())
else:
    print("Lỗi:", response.status_code, response.json())