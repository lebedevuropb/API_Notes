from api.base_api import BaseApi


class GetNote(BaseApi):
    ENDPOINT = "api/notes"

    def get_note(self, headers):
        return self.get(self.ENDPOINT, headers)
