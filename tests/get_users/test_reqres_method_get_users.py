import json
import pytest
import requests

from jsonschema import validate

from const import Const


@pytest.fixture(scope="function")
def send_get_all_users() -> requests.Response:
    get_all_users = requests.get(
        url="https://reqres.in/api/users",
        params={
            "page": 1,
            "per_page": 100
        },
        headers={
            "x-api-key": "reqres-free-v1"
        }
    )
    yield get_all_users


def test_get_all_users_and_check_pagination(send_get_all_users: requests.Response):
    response = send_get_all_users
    assert send_get_all_users.status_code == 200
    response_json = response.json()
    with open(f"{Const.SCHEMAS_DIR}/method_get_users_schema.json") as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    assert response_json["page"] == 1
    assert response_json["per_page"] == 100


def test_check_len_users_in_response_data(send_get_all_users: requests.Response):
    response = send_get_all_users
    assert send_get_all_users.status_code == 200
    response_json = response.json()
    with open(f"{Const.SCHEMAS_DIR}/method_get_users_schema.json") as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    assert len(response_json["data"]) == 12


def test_that_all_users_have_valid_emails_domain(send_get_all_users: requests.Response):
    response = send_get_all_users
    assert send_get_all_users.status_code == 200
    response_json = response.json()
    with open(f"{Const.SCHEMAS_DIR}/method_get_users_schema.json") as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    for user in response_json["data"]:
        assert user["email"].endswith("@reqres.in")


def test_that_all_users_have_parameter_avatar(send_get_all_users: requests.Response):
    response = send_get_all_users
    assert send_get_all_users.status_code == 200
    response_json = response.json()
    with open(f"{Const.SCHEMAS_DIR}/method_get_users_schema.json") as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    for user in response_json["data"]:
        assert user["avatar"]
        assert user["avatar"].startswith("https://reqres.in/img/faces/")
