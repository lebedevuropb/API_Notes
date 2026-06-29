from api.base_api import BaseApi


class DeleteNotesApi(BaseApi):
    ENDPOINT = "api/notes/"

    def delete_note(self, note_id, token=None):
        if token is None:
            return self.delete(self.ENDPOINT, note_id, headers=None)
        return self.delete(self.ENDPOINT, note_id, headers=token)
