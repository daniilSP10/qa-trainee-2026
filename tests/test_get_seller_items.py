class TestSellerItems:
    def test_get_items_for_seller(self, api_client, seller_id):
        api_client.create_item(seller_id, "Cat1", 100)
        api_client.create_item(seller_id, "Cat2", 200)
        resp = api_client.get_seller_items(seller_id)
        assert resp.status_code == 200
        items = resp.json()
        assert isinstance(items, list)
        assert len(items) >= 2
        for item in items:
            assert item["sellerId"] == seller_id

    def test_get_items_for_nonexistent_seller(self, api_client):
        resp = api_client.get_seller_items(999999999)
        assert resp.status_code == 200
        assert resp.json() == []