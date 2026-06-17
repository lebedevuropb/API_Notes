from lesson.lesson_18API.BaseAPI import BaseAPI
from lesson.lesson_18API.constants import NOTES_ENDPOINT, NOTE_BY_ID_ENDPOINT


class NotesAPI(BaseAPI):
    def get_notes(self, headers):
        return self.get(endpoint=NOTES_ENDPOINT, headers=headers)

    def post_notes(self, headers, content: str, title: str):
        body = {"content": content, "title": title}
        return self.post(endpoint=NOTES_ENDPOINT, headers=headers, json=body)

    def delete_note(self, headers, note_id):
        return self.delete(endpoint=NOTE_BY_ID_ENDPOINT.format(note_id=note_id), headers=headers)
