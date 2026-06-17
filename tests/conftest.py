import pytest

from lesson.lesson_18API.auth_api import AuthAPI


@pytest.fixture
def note_login():
    log = AuthAPI()
    response = log.login("lesson49@gmail.com", "qwerty123")
    token = response.json()['token']
    return {"Authorization": f"Bearer {token}"}
