class TestGetItem:
    def test_get_existing_item(self, api_client, created_item):
        item_id, seller_id, name, price = created_item
        resp = api_client.get_item(item_id)
        assert resp.status_code == 200
        data = resp.json()
        assert isinstance(data, list)
        assert len(data) == 1
        item = data[0]
        assert item["id"] == item_id
        assert item["sellerId"] == seller_id
        assert item["name"] == name
        assert item["price"] == price

    def test_get_nonexistent_item(self, api_client):
        resp = api_client.get_item("nonexistent")
        assert resp.status_code == 404