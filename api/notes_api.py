from base_api import BaseAPI


class Notes(BaseAPI):
    ENDPOINT = "api/notes"

    def get_notes(self, headers):
        return self.get(self.ENDPOINT, headers)
