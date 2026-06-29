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
        return login_api.get_token(email, password)

    return get_token


@pytest.fixture
def user_token(token):
    return token("loginpermonents@yandex.ru", "qwerty123")


@pytest.fixture
def second_token(token):
    return token("testcreatenotauthorized@yandex.ru", "qwerty123")


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
        "token": {"Authorization": "Bearer difgjerejklf"}
    }


@pytest.fixture
def id_note(post_note_api, get_note_api, user_token):
    title = generate_note_title()
    post_note_api.create_note(generate_note_content(), title, token=user_token)
    note_id = get_note_api.get_note_by_title(title, token=user_token)
    return note_id["id"]


@pytest.fixture
def teardown_note(delete_note_api, user_token):
    note_ids = []
    yield note_ids
    for note_id in note_ids:
        delete_note_api.delete_note(note_id, token=user_token)


@pytest.fixture
def setup_teardown_note(id_note, teardown_note):
    teardown_note.append(id_note)
    return id_note
