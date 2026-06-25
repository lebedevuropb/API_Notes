from base_api import BaseAPI


class PostNotesAPI(BaseAPI):
    ENDPOINT = "api/notes"

    def create_notes(self, headers, content: str, title: str):
        json = {"content": content, "title": title}
        return self.post(self.ENDPOINT, json, headers)
