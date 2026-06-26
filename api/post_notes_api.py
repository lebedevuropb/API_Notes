from api.authorized_api import AuthorizedApi


class PostNotesApi(AuthorizedApi):
    ENDPOINT = "api/notes"


    def headers(self):
        if self.token is None:
            return None
        return {"Authorization": f"Bearer {self.token}"}

    def create_note(self, content: str, title: str):
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, json=json, headers=self.headers())
