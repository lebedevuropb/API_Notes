# Создание заметки
def test_create_notes(obj_create_notes):
    assert obj_create_notes.status_code == 201
    assert obj_create_notes.json()["message"] == "Заметка создана!"
