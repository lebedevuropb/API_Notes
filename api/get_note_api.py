from api.authorized_api import AuthorizedApi


class GetNote(AuthorizedApi):
    ENDPOINT = "api/notes"

    def get_note(self, token=None):
        return self.get(self.ENDPOINT, headers=self.headers(token))

    def get_note_by_title(self, title, token=None):
        notes = self.get_note(token=token).json()
        for note in notes:
            if note["title"] == title:
                return note
        return None
