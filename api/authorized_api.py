from api.base_api import BaseApi



class AuthorizedApi(BaseApi):
    def token(self, token):
        return {"Authorization": f"Bearer {token}"}
