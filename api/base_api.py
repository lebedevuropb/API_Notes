import requests


class BaseApi:
    BASE_URL = "http://185.240.103.201:8000/"

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.BASE_URL}{endpoint}", headers=headers)

    def post(self, endpoint, json, headers=None):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=json, headers=headers)

    def delete(self, endpoint, note_id, headers):
        return requests.delete(f"{self.BASE_URL}{endpoint}{note_id}", headers=headers)
