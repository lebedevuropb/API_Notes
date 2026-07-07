from api.base_api import BaseApi


class LoginApi(BaseApi):
    ENDPOINT = "api/login"

    def login(self, email: str, password: str):
        json = {"email": email, "password": password}
        return self._requests(method="POST", endpoint=self.ENDPOINT, json=json)

    def get_token(self, email, password):
        response_json = self.login(email, password).json()
        return response_json["token"]
