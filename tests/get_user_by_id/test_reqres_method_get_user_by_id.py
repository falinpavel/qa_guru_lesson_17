import json
import os

import requests
import pytest

from jsonschema import validate
from utils.path_helpers import get_schema_path


USER = {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
}
SCHEMA_PATH = get_schema_path("method_get_user_by_id_schema.json")


@pytest.fixture(scope="function")
def send_get_user_by_id():
    response = requests.get(
        url=f"https://reqres.in/api/users/{USER['id']}",
        headers={
            "x-api-key": "reqres-free-v1"
        }
    )
    yield response


def test_mapping_data_user_in_response(send_get_user_by_id):
    response = send_get_user_by_id
    assert response.status_code == 200
    response_json = response.json()
    with open(SCHEMA_PATH) as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    assert response_json["data"]["id"] == USER["id"]
    assert response_json["data"]["email"] == USER["email"]
    assert response_json["data"]["first_name"] == USER["first_name"]
    assert response_json["data"]["last_name"] == USER["last_name"]
    assert response_json["data"]["avatar"] == USER["avatar"]


def test_block_support_present_in_response(send_get_user_by_id):
    response = send_get_user_by_id
    assert response.status_code == 200
    response_json = response.json()
    with open(SCHEMA_PATH) as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    assert response_json["support"]
    assert response_json["support"]["url"]
    assert response_json["support"]["text"]
