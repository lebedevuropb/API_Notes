from api.authorized_api import AuthorizedApi


class PostNotesApi(AuthorizedApi):
    ENDPOINT = "api/notes"

    def create_note(self, content: str, title: str, token=None):
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, json=json, headers=self.headers(token))
