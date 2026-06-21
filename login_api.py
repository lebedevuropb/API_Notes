from base_api import BaseAPI


class LoginAPI(BaseAPI):
    ENDPOINT = "api/login"

    def login(self, email: str, password: str):
        json = {"email": email, "password": password}
        return self.post(self.ENDPOINT, json)
