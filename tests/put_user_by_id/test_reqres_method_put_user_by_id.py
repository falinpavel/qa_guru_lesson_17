import os

import pytest
import requests
import json

from datetime import datetime
from jsonschema import validate
from utils.path_helpers import get_schema_path


USER = {
    "id": 2,
    "email": "janet.weaver@reqres.in",
    "first_name": "Janet",
    "last_name": "Weaver",
    "avatar": "https://reqres.in/img/faces/2-image.jpg"
}
SCHEMA_PATH = get_schema_path("method_put_user_by_id_schema.json")


def test_change_user_data_by_user_id():
    new_data = {
        "email": "janet_test.weaver@reqres.in",
        "first_name": "Janet_test",
        "last_name": "Weaver_test",
        "avatar": "https://reqres.in/img/faces/test.png"
    }
    response = requests.put(
        url=f"https://reqres.in/api/users/{USER['id']}",
        headers={
            "x-api-key": "reqres-free-v1"
        },
        json=new_data
    )
    response_json = response.json()
    with open(SCHEMA_PATH) as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    assert response.status_code == 200
    assert response_json["email"] == new_data["email"]
    assert response_json["first_name"] == new_data["first_name"]
    assert response_json["last_name"] == new_data["last_name"]
    assert response_json["avatar"] == new_data["avatar"]


@pytest.mark.xfail(
    reason="TASK-123 - изменение id пользователя должно быть невозможно методом PUT /api/users/{user_id}"
)
def test_that_user_id_not_changed():
    response = requests.put(
        url=f"https://reqres.in/api/users/{USER['id']}",
        headers={
            "x-api-key": "reqres-free-v1"
        },
        json={
            "id": None
        }
    )
    assert response.status_code == 400


def test_that_response_nas_parameter_updated_at():
    response = requests.put(
        url=f"https://reqres.in/api/users/{USER['id']}",
        headers={
            "x-api-key": "reqres-free-v1"
        },
        json={
            "email": "janet_test.weaver@reqres.in"
        }
    )
    response_json = response.json()
    with open(SCHEMA_PATH) as schema_file:
        validate(
            instance=response.json(),
            schema=json.loads(schema_file.read())
        )
    assert response_json["updatedAt"]
    assert response_json["updatedAt"].startswith(datetime.now().strftime("%Y-%m-%d"))
