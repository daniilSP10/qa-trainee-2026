import pytest
from utils.helpers import generate_seller_id

class TestNegativeCreate:
    def test_missing_seller_id(self, api_client):
        url = "https://qa-internship.avito.com/api/1/item"
        payload = {"name": "Cat", "price": 100}
        resp = api_client.session.post(url, json=payload)
        assert resp.status_code == 400

    def test_empty_name(self, api_client):
        resp = api_client.create_item(generate_seller_id(), "", 100)
        assert resp.status_code == 400

    def test_price_zero(self, api_client):
        resp = api_client.create_item(generate_seller_id(), "Cat", 0)
        assert resp.status_code in (400, 422)

    def test_price_negative(self, api_client):
        resp = api_client.create_item(generate_seller_id(), "Cat", -10)
        assert resp.status_code == 400

    def test_price_string(self, api_client):
        url = "https://qa-internship.avito.com/api/1/item"
        payload = {"sellerID": generate_seller_id(), "name": "Cat", "price": "abc"}
        resp = api_client.session.post(url, json=payload)
        assert resp.status_code == 400

    def test_seller_id_out_of_range(self, api_client):
        resp = api_client.create_item(1, "Cat", 100)
        assert resp.status_code == 400