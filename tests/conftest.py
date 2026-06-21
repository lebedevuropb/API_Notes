import pytest
from login_api import LoginAPI
from register_api import RegisterAPI
from notes_api import Notes
from post_notes_api import Post_notesAPI
from delete_notes_api import Delete_notesAPI
from tests.generation import generate_email, generate_username, generate_password, generate_note_content
from tests.generation import generate_note_title


@pytest.fixture
def obj_token(obj_login):
    response = obj_login.login("loginpermonents@yandex.ru", "qwerty123")
    token = response.json()["token"]
    return {"Authorization": f"Bearer {token}"}

# @pytest.fixture
# def obj_token_random(obj_login):
#     response = obj_login.login("loginpermonents@yandex.ru", "qwerty123")
#     token = response.json()["token"]
#     return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def random_user():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "username": generate_username()
    }


@pytest.fixture
def obj_random_register(obj_register):
    return obj_register.register(generate_email(), generate_password(), generate_username())


@pytest.fixture
def obj_authorization(obj_login):
    return obj_login.login("loginpermonents@yandex.ru", "qwerty123")


@pytest.fixture
def obj_register():
    return RegisterAPI()


@pytest.fixture
def obj_login():
    return LoginAPI()


@pytest.fixture
def obj_get_notes():
    return Notes()


@pytest.fixture
def obj_delete_notes():
    return Delete_notesAPI()

# @pytest.fixture
# def notes_id(obj_random_register):
#     return obj_random_register.json()[0]["id"]

# @pytest.fixture
# def obj_delete(obj_delete_notes, notes_id, obj_token):
#     pass


@pytest.fixture
def obj_list_notes(obj_get_notes, obj_token):
    response = obj_get_notes.get_notes(obj_token)
    return response.json()["data"]


@pytest.fixture
def obj_create_notes(obj_post_notes, obj_token, obj_get_notes, obj_delete_notes):
    response = obj_post_notes.create_notes(obj_token, generate_note_content(), generate_note_title())
    note_id = obj_get_notes.get_notes(obj_token).json()[0]["id"]
    yield response
    obj_delete_notes.delete_notes(note_id, obj_token)


@pytest.fixture
def obj_post_notes():
    return Post_notesAPI()
