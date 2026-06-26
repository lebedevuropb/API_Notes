from api.base_api import BaseApi


class AuthorizedApi(BaseApi):
    def __init__(self, token):
        self.token = token

    def headers(self, token=None):
        if token is None:
            token = self.token
        if token is None:
            return None
        return {"Authorization": f"Bearer {token}"}
