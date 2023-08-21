import requests
import pytest

headers = {'Cache-Control': 'None', 'Content-Type': 'application/json', 'User-Agent': 'app', 'Accept': '*/*'}
cars_endpoint = "https://car-fleet-management.herokuapp.com/cars/"


@pytest.fixture
def create_new_car_object():
	new_car = requests.post(cars_endpoint, headers=headers, json={
		"build": 2000,
		"manufacturer": "Honda",
		"model": "Accord"}).json()

	yield new_car
	generated_id = new_car["id"]
	delete_new_car_object(generated_id)


def delete_new_car_object(car_id):
	# Cleanup testdata
	res = requests.delete(f"{cars_endpoint}/{car_id}")
	assert res.ok
	assert res.status_code == 200
