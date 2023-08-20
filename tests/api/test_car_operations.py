from playwright.sync_api import sync_playwright

base_url = "https://car-fleet-management.herokuapp.com"


def test_get_all_cars():
	with sync_playwright() as p:
		api_request_context = p.request.new_context(base_url=base_url)
		response = api_request_context.get(
			"/cars",
			headers={
				"Accept": "*/*"
			}
		)
		assert response.ok
		assert response.status == 200


# assert response.body().count(4)


def test_get_car_by_id(create_new_car_object):
	with sync_playwright() as p:
		api_request_context = p.request.new_context(base_url=base_url)
		response = api_request_context.get(
			"/cars/1",
			headers={
				"Accept": "*/*"
			}
		)
		assert response.ok
		assert response.status == 200
		assert response.json()["manufacturer"] == "Ford"
		assert response.json()["model"] == "Model T"
		assert response.json()["build"] == 1927

# def test_create_a_new_car():
