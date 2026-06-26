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
    response = login_api.login("loginpermonents@yandex.ru", "qwerty123")
    return response.json()["token"]


@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def created_note(post_note_api, get_note_api, auth_headers):
    title = generate_note_title()
    content = generate_note_content()
    post_note_api.create_note(auth_headers, content, title)
    note = get_note_api.find_note_by_title(auth_headers, title)
    yield {"id": note["id"], "title": title}


@pytest.fixture
def note_for_delete(post_note_api, get_note_api, delete_note_api, auth_headers):
    title = generate_note_title()
    content = generate_note_content()
    post_note_api.create_note(auth_headers, content, title)
    note = get_note_api.find_note_by_title(auth_headers, title)
    yield note["id"]
    delete_note_api.delete_note(note["id"], auth_headers)


@pytest.fixture
def cleanup_note(delete_note_api, auth_headers):
    note_ids = []
    yield note_ids.append
    for note_id in note_ids:
        delete_note_api.delete_note(note_id, auth_headers)
