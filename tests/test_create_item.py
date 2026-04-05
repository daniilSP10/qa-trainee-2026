import allure
from utils.helpers import generate_seller_id, generate_item_name, generate_price

@allure.feature("Создание объявления")
class TestCreateItem:

    @allure.story("Позитивный сценарий")
    def test_create_valid_item(self, api_client):
        seller_id = generate_seller_id()
        name = generate_item_name()
        price = generate_price()
        resp = api_client.create_item(seller_id, name, price)
        print("STATUS:", resp.status_code)
        print("RESPONSE BODY:", resp.text)
        assert resp.status_code == 200
        data = resp.json()
        assert "id" in data
        assert data["sellerId"] == seller_id
        assert data["name"] == name
        assert data["price"] == price

    @allure.story("Граничные значения")
    def test_create_min_price(self, api_client):
        resp = api_client.create_item(generate_seller_id(), "Cat", 1)
        assert resp.status_code == 200

    def test_create_max_price(self, api_client):
        resp = api_client.create_item(generate_seller_id(), "Cat", 10**9)
        assert resp.status_code == 200

    def test_create_min_seller_id(self, api_client):
        resp = api_client.create_item(111111, "Cat", 100)
        assert resp.status_code == 200

    def test_create_max_seller_id(self, api_client):
        resp = api_client.create_item(999999, "Cat", 100)
        assert resp.status_code == 200