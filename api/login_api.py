from api.base_api import BaseApi


class LoginApi(BaseApi):
    ENDPOINT = "api/login"

    def login(self, email: str, password: str):
        json = {"email": email, "password": password}
        return self.post(self.ENDPOINT, json)
