from lesson.lesson_18API.BaseAPI import BaseAPI
from lesson.lesson_18API.constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT


class AuthAPI(BaseAPI):
    def register(self, email: str, password: str, username: str):
        body = {"email": email, "password": password, "username": username}
        return self.post(endpoint=REGISTER_ENDPOINT, json=body)

    def login(self, email: str, password: str):
        body = {"email": email, "password": password}
        return self.post(endpoint=LOGIN_ENDPOINT, json=body)
