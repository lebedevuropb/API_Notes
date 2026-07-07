import requests


class BaseApi:
    BASE_URL = "http://185.240.103.201:8000/"
    token = None

    def _requests(self, method: str, endpoint=None, note_id=None, need_token=False, json=None):
        if note_id:
            url = f"{self.BASE_URL}{endpoint}/{note_id}"
        else:
            url = f"{self.BASE_URL}{endpoint}"
        return requests.request(method, url=url, headers=self._header(need_token), json=json)

    def _header(self, need_token=False):
        if need_token:
            return {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.token}"}
        else:
            return {
                "Accept": "application/json",
                "Content-Type": "application/json"}
