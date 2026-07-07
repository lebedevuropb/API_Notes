from api.base_api import BaseApi


class GetNote(BaseApi):
    ENDPOINT = "api/notes"

    def __init__(self, token):
        self.token = token

    def get_note(self):
        return self._requests(method="GET", endpoint=self.ENDPOINT, need_token=bool(self.token))

    def get_note_by_title(self, title):
        notes = self.get_note().json()
        for note in notes:
            if note["title"] == title:
                return note
        return None
