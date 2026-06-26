from api.base_api import BaseApi


class AuthorizedApi(BaseApi):
    def __init__(self, token):
        self.token = token

    def headers(self):
        if self.token is None:
            return None
        return {"Authorization": f"Bearer {self.token}"}
