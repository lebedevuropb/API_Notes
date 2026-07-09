from api.base_api import BaseApi


class DeleteNotesApi(BaseApi):
    ENDPOINT = "api/notes"

    def __init__(self, token):
        self.token = token

    def delete_note(self, note_id, need_toke=True):
        return self._requests(method="DELETE", endpoint=self.ENDPOINT, note_id=note_id, need_token=need_toke)
