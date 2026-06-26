from api.base_api import BaseApi


class GetNote(BaseApi):
    ENDPOINT = "api/notes"

    def get_note(self, headers):
        return self.get(self.ENDPOINT, headers)

    def find_note_by_title(self, headers, title: str):
        notes = self.get_note(headers).json()
        for note in notes:
            if note["title"] == title:
                return note
        return None
