from api.authorized_api import AuthorizedApi


class PostNotesApi(AuthorizedApi):
    ENDPOINT = "api/notes"

    def create_note(self, content: str, title: str, token=None):
        json = {"content": content, "title": title}
        if token is None:
            return self.get(self.ENDPOINT)
        return self.post(self.ENDPOINT, json=json, headers=self.token(token))
