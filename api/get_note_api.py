from api.authorized_api import AuthorizedApi


class GetNote(AuthorizedApi):
    ENDPOINT = "api/notes"

    def get_note(self):
        return self.get(self.ENDPOINT, headers=self.headers())

    def get_note_by_title(self, title):
        notes = self.get_note().json()
        for note in notes:
            if note["title"] == title:
                return note
        return None
