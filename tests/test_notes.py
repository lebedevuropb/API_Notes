from utils.generation import generate_note_title, generate_note_content


# Позитивные проверки

# Создание заметки
def test_create_note(teardown_note, post_note_api, get_note_api, user_token):
    title = generate_note_title()
    response = post_note_api.create_note(generate_note_content(), title, token=user_token)
    note = get_note_api.get_note_by_title(title, token=user_token)
    teardown_note.append(note["id"])

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    assert response.json()["message"] == "Заметка создана!", "Отсутствует сообщение 'Заметка создана!'"


# Проверка заметки
def test_get_all_notes(get_note_api, setup_teardown_note, user_token):
    response = get_note_api.get_note(token=user_token)
    notes = response.json()

    for note in notes:
        assert "content" in note, "В одной из заметок отсутствует поле «content»"
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"


# Проверка удаления
def test_delete_note(id_note, delete_note_api, user_token):
    response = delete_note_api.delete_note(id_note, token=user_token)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert response.json()["message"] == "Note deleted!", "Отсутствует сообщение «Note deleted»"


# Негативные проверки

# Получение заметок без токена
def test_get_notes_unauthorized(none_token):
    response = none_token["get"].get_note()

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Token is missing!", "Отсутствует сообщение 'Token is missing!'"


# Получение заметок с невалидным токеном
def test_get_notes_forbidden(invalid_token):
    response = invalid_token["get"].get_note(token=invalid_token["token"])

    assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
    assert response.json()["message"] == "Token is invalid or expired!", \
        "Отсутствует сообщение 'Token is invalid or expired!'"


# Создание заметки без токена
def test_create_note_unauthorized(none_token):
    response = none_token["post"].create_note(generate_note_content(), generate_note_title())

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Token is missing!", "Отсутствует сообщение 'Token is missing!'"


# Создание заметки с невалидным токеном
def test_create_note_forbidden(invalid_token):
    response = invalid_token["delete"].delete_note(5321, token=invalid_token["token"])

    assert response.status_code == 403, f"Ожидался статус 403, получен {response.status_code}"
    assert response.json()["message"] == "Token is invalid or expired!", \
        "Отсутствует сообщение 'Token is invalid or expired!'"


# Удаление заметки без токена
def test_delete_note_unauthorized(none_token):
    response = none_token["delete"].delete_note(5477)

    assert response.status_code == 401, f"Ожидался статус 401, получен {response.status_code}"
    assert response.json()["message"] == "Token is missing!", "Отсутствует сообщение 'Token is missing!'"


# Удаление заметки пользователю не преналежит
def test_del_notes_resource_conflict(setup_teardown_note, second_token, delete_note_api):
    response = delete_note_api.delete_note(setup_teardown_note, token=second_token)

    assert response.status_code == 409, f"Ожидался статус 409, получен {response.status_code}"
    assert response.json()["message"] == "Not authorized to delete this note", \
        "Отсутствует сообщение «Not authorized to delete this note»"
