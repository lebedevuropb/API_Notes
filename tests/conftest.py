import pytest
from api.login_api import LoginApi
from api.register_api import RegisterAPI
from api.notes_api import Notes
from api.post_notes_api import PostNotesAPI
from api.delete_notes_api import DeleteNotesApi
from tests.generation import generate_email, generate_username, generate_password, generate_note_content
from tests.generation import generate_note_title


@pytest.fixture
def obj_register():
    return RegisterAPI()


@pytest.fixture
def obj_login():
    return LoginApi()


@pytest.fixture
def obj_get_notes():
    return Notes()


@pytest.fixture
def obj_delete_notes():
    return DeleteNotesApi()


@pytest.fixture
def obj_post_notes():
    return PostNotesApi()


@pytest.fixture
def token(obj_login):
    response = obj_login.login("loginpermonents@yandex.ru", "qwerty123")
    return response.json()["token"]


@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def cleanup_note(obj_delete_notes, auth_headers):
    note_ids = []
    yield note_ids.append
    for note_id in note_ids:
        obj_delete_notes.delete_note(auth_headers, note_id)


@pytest.fixture
def random_user():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "username": generate_username()
    }
