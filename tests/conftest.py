import pytest
from api.login_api import LoginApi
from api.register_api import RegisterApi
from api.get_note_api import GetNote
from api.post_notes_api import PostNotesApi
from api.delete_notes_api import DeleteNotesApi
from utils.generation import generate_note_title, generate_note_content
from api.authorized_api import AuthorizedApi


@pytest.fixture
def register_api():
    return RegisterApi()


@pytest.fixture
def login_api():
    return LoginApi()


@pytest.fixture
def authorized_api():
    return AuthorizedApi()


@pytest.fixture
def get_note_api():
    return GetNote()


@pytest.fixture
def delete_note_api():
    return DeleteNotesApi()


@pytest.fixture
def post_note_api():
    return PostNotesApi()


@pytest.fixture
def token(login_api):
    def get_token(email, password):
        response = login_api.login(email, password)
        return response.json()["token"]

    return get_token


@pytest.fixture
def user_token(token):
    return token("loginpermonents@yandex.ru", "qwerty123")


@pytest.fixture
def none_token():
    return {
        "get": GetNote(),
        "post": PostNotesApi(),
        "delete": DeleteNotesApi()
    }


@pytest.fixture
def invalid_token():
    return {
        "get": GetNote(),
        "post": PostNotesApi(),
        "delete": DeleteNotesApi(),
        "token": "difgjerejklf"
    }


@pytest.fixture
def created_note(post_note_api, get_note_api, user_token):
    title = generate_note_title()
    post_note_api.create_note(generate_note_content(), title, token=user_token)
    note_id = get_note_api.get_note_by_title(title, token=user_token)
    return note_id["id"]


@pytest.fixture
def cleanup_created_note(get_note_api, delete_note_api, user_token):
    notes_before = get_note_api.get_note(token=user_token).json()
    ids_before = [note["id"] for note in notes_before]
    yield
    notes_after = get_note_api.get_note(token=user_token).json()
    for note in notes_after:
        if note["id"] not in ids_before:
            delete_note_api.delete_note(note["id"], token=user_token)


@pytest.fixture
def cleanup_get_note(post_note_api, cleanup_created_note, user_token):
    post_note_api.create_note(generate_note_content(), generate_note_title(), token=user_token)
    yield


@pytest.fixture
def delete_note_not_authorized(login_api, get_note_api, post_note_api, delete_note_api):
    token_guest = login_api.login("testcreatenotauthorized@yandex.ru", "qwerty123").json()["token"]
    title = generate_note_title()
    post_note_api.create_note(generate_note_content(), title, token=token_guest)
    note_guest = get_note_api.get_note_by_title(title, token=token_guest)

    yield note_guest["id"]

    delete_note_api.delete_note(note_guest["id"], token=token_guest)
