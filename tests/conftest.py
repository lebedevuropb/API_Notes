import pytest
from api.login_api import LoginApi
from api.register_api import RegisterApi
from api.get_note_api import GetNote
from api.post_notes_api import PostNotesApi
from api.delete_notes_api import DeleteNotesApi
from utils.generation import generate_note_title, generate_note_content


@pytest.fixture
def register_api():
    return RegisterApi()


@pytest.fixture
def login_api():
    return LoginApi()


@pytest.fixture
def get_note_api(token):
    return GetNote(token)


@pytest.fixture
def delete_note_api(token):
    return DeleteNotesApi(token)


@pytest.fixture
def post_note_api(token):
    return PostNotesApi(token)


@pytest.fixture
def token(login_api):
    response = login_api.login("loginpermonents@yandex.ru", "qwerty123")
    return response.json()["token"]


@pytest.fixture
def none_token():
    return {
        "get": GetNote(None),
        "post": PostNotesApi(None),
        "delete": DeleteNotesApi(None),
    }


@pytest.fixture
def invalid_token():
    return {
        "get": GetNote("difgjerejklf"),
        "post": PostNotesApi("difgjerejklf"),
        "delete": DeleteNotesApi("difgjerejklf"),
    }


@pytest.fixture
def created_note(post_note_api, get_note_api):
    title = generate_note_title()
    post_note_api.create_note(generate_note_content(), title)
    note_id = get_note_api.get_note_by_title(title)
    return note_id["id"]


@pytest.fixture
def cleanup_created_note(get_note_api, delete_note_api):
    notes_before = get_note_api.get_note().json()
    ids_before = [note["id"] for note in notes_before]
    yield
    notes_after = get_note_api.get_note().json()
    for note in notes_after:
        if note["id"] not in ids_before:
            delete_note_api.delete_note(note["id"])


@pytest.fixture
def cleanup_get_note(post_note_api, cleanup_created_note):
    post_note_api.create_note(generate_note_content(), generate_note_title())
    yield
