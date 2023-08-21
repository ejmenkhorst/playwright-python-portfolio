from playwright.sync_api import sync_playwright
from tests.conftest import delete_new_car_object, create_new_car_object, cars_endpoint


def test_get_all_cars():
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url=cars_endpoint)
        response = api_request_context.get(
            "/cars",
            headers={
                "Accept": "*/*"
            }
        )
        assert response.ok
        assert response.status == 200


def test_get_car_by_id():
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url=cars_endpoint)
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


def test_create_a_new_car():
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url=cars_endpoint)
        response = api_request_context.post(
            "/cars/",
            headers={
                "Accept": "*/*"
            },
            data={
                "build": 1990,
                "manufacturer": "Suzuki",
                "model": "Swift 1.2"})

        assert response.ok
        assert response.status == 200
        assert response.json()["manufacturer"] == "Suzuki"
        assert response.json()["model"] == "Swift 1.2"
        assert response.json()["build"] == 1990

        # cleanup testdata
        generated_id = response.json()["id"]
        delete_new_car_object(generated_id)


def test_update_car(create_new_car_object):
    # Arrange
    new_car = create_new_car_object

    # Act
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url=cars_endpoint)
        response = api_request_context.put(
            "/cars/",
            headers={
                "Accept": "*/*"
            },
            data={
                "build": 1990,
                "id": new_car["id"],
                "manufacturer": "Nissan",
                "model": "Sunny"})

    # Assert
        assert response.ok
        assert response.status == 200
        assert response.json()["manufacturer"] == "Nissan"
        assert response.json()["model"] == "Sunny"
        assert response.json()["build"] == 1990
