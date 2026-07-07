from api.base_api import BaseApi


class RegisterApi(BaseApi):
    ENDPOINT = "api/register"

    def register(self, email: str, password: str, username: str):
        json = {"email": email, "password": password, "username": username}
        return self._requests(method="POST", endpoint=self.ENDPOINT, json=json)
