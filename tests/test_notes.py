from utils.generation import generate_note_title, generate_note_content


# Позитивные проверки

# Создание заметки
def test_create_note(auth_headers, obj_post_notes, obj_get_notes, cleanup_note):
    title = generate_note_title()
    response = obj_post_notes.create_note(auth_headers, generate_note_content(), title)

    assert response.status_code == 201, f"Ожидался статус 201, получен {response.status_code}"
    assert response.json()["message"] == "Заметка создана!", "Отсутствует сообщение 'Заметка создана!'"

    note_id = obj_get_notes.get_note(auth_headers).json()
    for note in note_id:
        if note["title"] == title:
            cleanup_note(note["id"])


# Проверка заметки
def test_get_all_notes(auth_headers, obj_get_notes):
    response = obj_get_notes.get_note(auth_headers)

    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert "content" in response.json()[0], "В ответе отсутствует поле «content»"


# Проверка удаления
def test_delete_note(obj_delete_notes, create_notes, auth_headers, obj_get_notes):
    assert create_notes.status_code == 201, f"Ожидался статус 201, получен {create_notes.status_code}"

    note_id = obj_get_notes.get_note(auth_headers).json()[0]["id"]
    response = obj_delete_notes.delete_note(note_id, auth_headers)

    assert response.status_code == 200
