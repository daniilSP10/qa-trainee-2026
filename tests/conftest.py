import pytest
from utils.api_client import ApiClient
from utils.helpers import generate_seller_id

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()

@pytest.fixture
def seller_id():
    return generate_seller_id()

@pytest.fixture
def created_item(api_client, seller_id):
    name = "Test Cat"
    price = 5000
    resp = api_client.create_item(seller_id, name, price)
    assert resp.status_code == 200, f"Failed to create item: {resp.text}"
    item_data = resp.json()
    item_id = item_data["id"]
    yield item_id, seller_id, name, price
    
    api_client.delete_item(item_id)