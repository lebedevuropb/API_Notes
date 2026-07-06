from api.base_api import BaseApi


class PostNotesApi(BaseApi):
    ENDPOINT = "api/notes"

    def __init__(self, token):
        self.token = token

    def create_note(self, content: str, title: str):
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, json=json, headers=self.token)
