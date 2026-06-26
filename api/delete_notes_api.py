from api.authorized_api import AuthorizedApi


class DeleteNotesApi(AuthorizedApi):
    ENDPOINT = "api/notes/"


    def headers(self):
        if self.token is None:
            return None
        return {"Authorization": f"Bearer {self.token}"}

    def delete_note(self, note_id):
        return self.delete(self.ENDPOINT, note_id, headers=self.headers())
