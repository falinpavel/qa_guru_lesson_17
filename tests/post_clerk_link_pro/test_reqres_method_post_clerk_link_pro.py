from datetime import datetime

import pytest
import requests

EMAIL = "falin.p@test.ru"


@pytest.fixture(scope="function")
def send_post_request():
    response = requests.post(
        url="https://reqres.in/api/users",
        headers={
            "x-api-key": "reqres-free-v1"
        },
        json={
            "email": EMAIL
        }
    )
    yield response


def test_send_email_and_get_your_id(send_post_request):
    response = send_post_request
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["id"]


def test_send_email_and_check_that_parameter_created_at_is_present(send_post_request):
    response = send_post_request
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["createdAt"]
    assert response_json["createdAt"].startswith(datetime.now().strftime("%Y-%m-%d"))


def test_send_email_and_check_that_sent_email_is_correct(send_post_request):
    response = send_post_request
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["email"] == EMAIL
