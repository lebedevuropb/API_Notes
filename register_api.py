from base_api import BaseAPI


class RegisterAPI(BaseAPI):
    ENDPOINT = "api/register"

    def register(self, email: str, password: str, username: str):
        json = {"email": email, "password": password, "username": username}
        return self.post(self.ENDPOINT, json)
