from api.base_api import BaseApi


class PostNotesApi(BaseApi):
    ENDPOINT = "api/notes"

    def create_note(self, content: str, title: str, token=None):
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, json=json, headers=token)
