import requests

USER_ID = 2


def test_delete_user_by_id():
    response = requests.delete(
        url=f"https://reqres.in/api/users/{USER_ID}",
        headers={
            "x-api-key": "reqres-free-v1"
        }
    )
    assert response.status_code == 204

