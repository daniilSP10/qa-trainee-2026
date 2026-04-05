class TestStatistic:
    def test_statistic_exists(self, api_client, created_item):
        item_id, _, _, _ = created_item
        resp = api_client.get_statistic_v1(item_id)
        assert resp.status_code == 200
        stats = resp.json()
        assert isinstance(stats, list)
        assert len(stats) > 0
        first = stats[0]
        assert "likes" in first
        assert "viewCount" in first
        assert "contacts" in first
        assert isinstance(first["likes"], int)
        assert isinstance(first["viewCount"], int)

    def test_statistic_not_found(self, api_client):
        resp = api_client.get_statistic_v1("invalid_id")
        assert resp.status_code == 404