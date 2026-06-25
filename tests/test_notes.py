from utils.generation import generate_email, generate_note_title, generate_note_content, generate_password, generate_username


# Позитивные проверки

# Создание заметки
def test_create_note(auth_headers, post_note_api, get_note_api, cleanup_note):
    title = generate_note_title()
    response = post_note_api.create_note(auth_headers, generate_note_content(), title)

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    assert response.json()["message"] == "Заметка создана!", "Отсутствует сообщение 'Заметка создана!'"

    note = get_note_api.find_note_by_title(auth_headers, title)
    cleanup_note(note["id"])


# Проверка заметки
def test_get_all_notes(auth_headers, get_note_api, delete_note_api, created_note):
    response = get_note_api.get_note(auth_headers)
    note = get_note_api.find_note_by_title(auth_headers, created_note["title"])

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert "content" in note, "В ответе отсутствует поле «content»"

    delete_note_api.delete_note(created_note["id"], auth_headers)


# Проверка удаления
def test_delete_note(delete_note_api, note_for_delete, auth_headers):
    response = delete_note_api.delete_note(note_for_delete, auth_headers)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"


# Негативные проверки

# Получение заметок без токена
def test_get_notes_unauthorized(get_note_api):
    response = get_note_api.get_note(None)

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Token is missing!", "Отсутствует сообщение 'Token is missing!'"


# Получение заметок с невалидным токеном
def test_get_notes_forbidden(get_note_api):
    response = get_note_api.get_note({"Authorization": "Bearer invalid_token"})

    assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
    assert response.json()["message"] == "Token is invalid or expired!", \
        "Отсутствует сообщение 'Token is invalid or expired!'"


# Создание заметки без токена
def test_create_note_unauthorized(post_note_api):
    response = post_note_api.create_note(None, generate_note_content(), generate_note_title())

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Token is missing!", "Отсутствует сообщение 'Token is missing!'"


# Создание заметки с невалидным токеном
def test_create_note_forbidden(post_note_api):
    response = post_note_api.create_note(
        {"Authorization": "Bearer invalid_token"},
        generate_note_content(),
        generate_note_title()
    )

    assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
    assert response.json()["message"] == "Token is invalid or expired!", \
        "Отсутствует сообщение 'Token is invalid or expired!'"


# Удаление заметки без токена
def test_delete_note_unauthorized(delete_note_api):
    response = delete_note_api.delete_note(1, None)

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Token is missing!", "Отсутствует сообщение 'Token is missing!'"


# Удаление заметки с невалидным токеном
def test_delete_note_forbidden(delete_note_api):
    response = delete_note_api.delete_note(1, {"Authorization": "Bearer invalid_token"})

    assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
    assert response.json()["message"] == "Token is invalid or expired!", \
        "Отсутствует сообщение 'Token is invalid or expired!'"


# Удаление чужой заметки
def test_delete_note_not_authorized(
    register_api, login_api, post_note_api, get_note_api, delete_note_api, auth_headers
):
    email = generate_email()
    password = generate_password()
    username = generate_username()
    register_api.register(email, password, username)

    other_token = login_api.login(email, password).json()["token"]
    other_headers = {"Authorization": f"Bearer {other_token}"}

    title = generate_note_title()
    post_note_api.create_note(other_headers, generate_note_content(), title)
    note = get_note_api.find_note_by_title(other_headers, title)
    note_id = note["id"]

    response = delete_note_api.delete_note(note_id, auth_headers)

    assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
    assert response.json()["message"] == "Not authorized to delete this note", \
        "Отсутствует сообщение 'Not authorized to delete this note'"

    delete_note_api.delete_note(note_id, other_headers)
