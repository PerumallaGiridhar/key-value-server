import pytest
import timeit
from fastapi.testclient import TestClient

from load_data import get_lookup_data
from config import DATA_FILE_PATH
from main import app


def timeit_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} execution time: {elapsed_time:.6f} seconds")
        return result
    return wrapper


class TestSetup:
    client = TestClient(app)
    lookup = get_lookup_data(DATA_FILE_PATH)

    def test_client(self):
        response = self.client.get('/')
        assert response.status_code == 200


class TestKeyValue:
    def test_read_item_valid_uuid(self):
        """
        Testing valid uuid in lookup
        """
        item_id = list(TestSetup.lookup.keys())[0]
        response = TestSetup.client.get(f"/items/{item_id}")
        assert response.status_code == 200
        assert response.json() == {str(item_id): TestSetup.lookup[item_id]}

    def test_read_item_invalid_uuid(self):
        """
        Testing invalid uuid
        """
        invalid_uuid = "invalid-uuid"
        response = TestSetup.client.get(f"/items/{invalid_uuid}")
        assert response.status_code == 422

    def test_read_item_not_in_lookup(self):
        """
        Testing valid uuid not in lookup
        """
        item_id_not_in_lookup = "00000000-0000-0000-0000-000000000000"
        response = TestSetup.client.get(f"/items/{item_id_not_in_lookup}")
        assert response.status_code == 404
        assert response.json() == {'detail': f"Item with ID {item_id_not_in_lookup} not found"}


class TestTearDown:
    pass




@timeit_wrapper
def read_item_valid_uuid():
    """
    calculating time taken for a valid uuid in lookup
    """
    item_id = list(TestSetup.lookup.keys())[0]
    response = TestSetup.client.get(f"/items/{item_id}")


if __name__ == "__main__":
    # run this file directly to understand the time taken for lookup
    # other wise you should use pytest
    read_item_valid_uuid()

