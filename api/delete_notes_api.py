from api.authorized_api import AuthorizedApi


class DeleteNotesApi(AuthorizedApi):
    ENDPOINT = "api/notes/"

    def delete_note(self, note_id, token=None):
        if token is None:
            return self.get(self.ENDPOINT)
        return self.delete(self.ENDPOINT, note_id, headers=self.token(token))
