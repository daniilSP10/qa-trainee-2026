class TestE2E:
    def test_full_lifecycle(self, api_client):
        seller_id = 123456
        name = "E2E Cat"
        price = 777
        create_resp = api_client.create_item(seller_id, name, price)
        assert create_resp.status_code == 200
        item_id = create_resp.json()["id"]

        get_resp = api_client.get_item(item_id)
        assert get_resp.status_code == 200
        item = get_resp.json()[0]
        assert item["name"] == name

        stat_resp = api_client.get_statistic_v1(item_id)
        assert stat_resp.status_code == 200
        initial_views = stat_resp.json()[0]["viewCount"]

        api_client.get_item(item_id)

        stat_resp2 = api_client.get_statistic_v1(item_id)
        new_views = stat_resp2.json()[0]["viewCount"]
        assert new_views == initial_views + 1

        del_resp = api_client.delete_item(item_id)
        assert del_resp.status_code == 200

        final_get = api_client.get_item(item_id)
        assert final_get.status_code == 404