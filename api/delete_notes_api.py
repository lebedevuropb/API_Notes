from api.authorized_api import AuthorizedApi


class DeleteNotesApi(AuthorizedApi):
    ENDPOINT = "api/notes/"

    def delete_note(self, note_id, token=None):
        return self.delete(self.ENDPOINT, note_id, headers=self.headers(token))
