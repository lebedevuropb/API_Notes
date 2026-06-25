from base_api import BaseAPI


class DeleteNotesApi(BaseAPI):
    ENDPOINT = "api/notes/"

    def delete_note(self, note_id, headers):
        return self.delete(self.ENDPOINT, note_id, headers)
