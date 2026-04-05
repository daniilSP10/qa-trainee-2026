class TestDeleteItem:
    def test_delete_existing_item(self, api_client, created_item):
        item_id, _, _, _ = created_item
        resp = api_client.delete_item(item_id)
        assert resp.status_code == 200
        get_resp = api_client.get_item(item_id)
        assert get_resp.status_code == 404

    def test_delete_nonexistent_item(self, api_client):
        resp = api_client.delete_item("nonexistent_id")
        assert resp.status_code == 404