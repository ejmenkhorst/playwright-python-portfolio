import requests
import pytest

headers = {'Cache-Control': 'None', 'Content-Type': 'application/json', 'User-Agent': 'app', 'Accept': '*/*'}
cars_endpoint = "https://car-fleet-management.herokuapp.com/cars/"


@pytest.fixture
def create_new_car_object():
	data = requests.post(cars_endpoint, json={"build": 2010, "manufacturer": "JAHAHA", "model": "MUHAHA"},
						 headers=headers).json()
	yield
	generated_id = data["id"]
	return print(f"Car which was generated with ID: {generated_id} data from response created car: {data}")
	requests.delete(cars_endpoint, json={})
