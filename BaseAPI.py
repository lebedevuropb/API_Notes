import requests
from lesson.lesson_18API.constants import BASE_URL


class BaseAPI:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)

    def post(self, endpoint, json=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", headers=headers, json=json)

    def delete(self, endpoint, headers=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
