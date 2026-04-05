import requests

BASE_URL = "https://qa-internship.avito.com"

class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def create_item(self, seller_id: int, name: str, price: int):
        url = f"{BASE_URL}/api/1/item"
        # Пробовали разные варианты, все возвращают 400
        # Вариант 1: statistics как объект (строки)
        payload = {
            "sellerID": str(seller_id),
            "name": name,
            "price": str(price),
            "statistics": {
                "likes": "0",
                "viewCount": "0",
                "contacts": "0"
            }
        }
        # Вариант 2: поля на верхнем уровне (строки)
        # payload = {
        #     "sellerID": str(seller_id),
        #     "name": name,
        #     "price": str(price),
        #     "likes": "0",
        #     "viewCount": "0",
        #     "contacts": "0"
        # }
        print(">>> Sending payload:", payload)  # для отладки
        response = self.session.post(url, json=payload)
        return response

    def get_item(self, item_id: str):
        url = f"{BASE_URL}/api/1/item/{item_id}"
        return self.session.get(url)

    def get_seller_items(self, seller_id: int):
        url = f"{BASE_URL}/api/1/{seller_id}/item"
        return self.session.get(url)

    def get_statistic_v1(self, item_id: str):
        url = f"{BASE_URL}/api/1/statistic/{item_id}"
        return self.session.get(url)

    def delete_item(self, item_id: str):
        url = f"{BASE_URL}/api/2/item/{item_id}"
        return self.session.delete(url)

    def get_statistic_v2(self, item_id: str):
        url = f"{BASE_URL}/api/2/statistic/{item_id}"
        return self.session.get(url)