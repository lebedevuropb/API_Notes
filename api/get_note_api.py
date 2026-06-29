from api.base_api import BaseApi


class GetNote(BaseApi):
    ENDPOINT = "api/notes"

    def get_note(self, token=None):
        if token is None:
            return self.get(self.ENDPOINT)
        return self.get(self.ENDPOINT, headers=token)

    def get_note_by_title(self, title, token=None):
        notes = self.get_note(token=token).json()
        for note in notes:
            if note["title"] == title:
                return note
        return None
