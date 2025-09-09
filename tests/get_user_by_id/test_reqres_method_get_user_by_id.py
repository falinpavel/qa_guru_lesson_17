import requests

USER = {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
}


def test_mapping_data_user_in_response():
    response = requests.get(
        url=f"https://reqres.in/api/users/{USER['id']}",
        headers={"x-api-key": "reqres-free-v1"}
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["data"]["id"] == USER["id"]
    assert response_json["data"]["email"] == USER["email"]
    assert response_json["data"]["first_name"] == USER["first_name"]
    assert response_json["data"]["last_name"] == USER["last_name"]
    assert response_json["data"]["avatar"] == USER["avatar"]


def test_block_support_present_in_response():
    response = requests.get(
        url=f"https://reqres.in/api/users/{USER['id']}",
        headers={"x-api-key": "reqres-free-v1"}
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["support"]
    assert response_json["support"]["url"]
    assert response_json["support"]["text"]
