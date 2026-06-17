from lesson.lesson_18API.notes_api import NotesAPI


def test_create_note(note_login):
    create = NotesAPI()
    response = create.post_notes(note_login, "Моя тестовая заметка, для проверки", "Тест заметка")

    assert response.status_code == 201


def test_notes(note_login):
    notes = NotesAPI()
    response = notes.get_notes(note_login)

    assert response.status_code == 200


def test_deleted_note(note_login):
    notes = NotesAPI()
    response1 = notes.get_notes(note_login)
    id_note = response1.json()[0]["id"]
    delet = NotesAPI()
    response2 = delet.delete_note(note_login, id_note)

    assert response2.status_code == 200
