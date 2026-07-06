import pytest
from api.login_api import LoginApi
from api.register_api import RegisterApi
from api.get_note_api import GetNote
from api.post_notes_api import PostNotesApi
from api.delete_notes_api import DeleteNotesApi
from utils.generation import generate_note_title, generate_note_content
from config.credentials import EMAIL, PASSWORD, SECOND_EMAIL, INVALID_TOKEN


@pytest.fixture
def register_api():
    return RegisterApi()


@pytest.fixture
def login_api():
    return LoginApi()


@pytest.fixture
def get_note_api(user_token):
    return GetNote(user_token)


@pytest.fixture
def get_note_api_without_token():
    return GetNote(None)


@pytest.fixture
def get_note_api_with_invalid_token():
    return GetNote(INVALID_TOKEN)


@pytest.fixture
def post_note_api_without_token():
    return PostNotesApi(None)


@pytest.fixture
def post_note_api_with_invalid_token():
    return PostNotesApi(INVALID_TOKEN)


@pytest.fixture
def delete_note_api():
    return DeleteNotesApi()


@pytest.fixture
def post_note_api(user_token):
    return PostNotesApi(user_token)


@pytest.fixture
def user_token(login_api):
    response = login_api.get_token(EMAIL, PASSWORD)
    return response


@pytest.fixture
def second_token(login_api):
    response = login_api.get_token(SECOND_EMAIL, PASSWORD)
    return response


@pytest.fixture
def id_note(post_note_api, get_note_api):
    title = generate_note_title()
    post_note_api.create_note(generate_note_content(), title)
    note_id = get_note_api.get_note_by_title(title)
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
