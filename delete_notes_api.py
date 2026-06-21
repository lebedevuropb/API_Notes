from base_api import BaseAPI


class Delete_notesAPI(BaseAPI):
    ENDPOINT = "api/notes/"

    def delete_notes(self, note_id, headers):
        return self.delete(self.ENDPOINT, note_id, headers)
