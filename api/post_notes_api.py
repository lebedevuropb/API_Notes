from api.base_api import BaseApi


class PostNotesApi(BaseApi):
    ENDPOINT = "api/notes"

    def __init__(self, token):
        self.token = token

    def create_note(self, content: str, title: str, need_toke=True):
        json = {"content": content, "title": title}
        return self._requests(method="POST", endpoint=self.ENDPOINT, need_token=need_toke, json=json)
