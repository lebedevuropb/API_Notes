from api.base_api import BaseApi


class PostNotesApi(BaseApi):
    ENDPOINT = "api/notes"

    def create_note(self, content: str, title: str, token=None):
        json = {"content": content, "title": title}
        if token is None:
            return self.get(self.ENDPOINT)
        return self.post(self.ENDPOINT, json=json, headers=token)
