from api.base_api import BaseApi


class Notes(BaseApi):
    ENDPOINT = "api/notes"

    def get_note(self, headers):
        return self.get(self.ENDPOINT, headers)
