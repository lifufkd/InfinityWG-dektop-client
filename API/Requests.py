##########################
#       Created By       #
#          SBR           #
##########################
import requests
from typing import Optional
from utilities.config import Config
##########################

##########################


class Authorization:
    def __init__(self, config: Config):
        super().__init__()
        self._token = config.get(config.token)
        self._config = config

    def get_host_url(self):
        return self._config.get(self._config.host)

    def check_token(self) -> Optional[dict]:
        host_url = self.get_host_url()
        request_url = host_url + "/users/check/token"
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        response = requests.get(request_url, headers=headers)
        if response.status_code == 200:
            return {"status": True, **response.json()}
        else:
            return {"status": False, **response.json()}

    def login(self, login: str, password: str, remember_me: bool) -> Optional[dict]:
        host_url = self.get_host_url()
        request_url = host_url + "/users/login"
        data = {
            "username": login,
            "password": password
        }
        response = requests.post(request_url, data=data)
        if response.status_code == 200:
            self._token = response.json()['access_token']
            if remember_me:
                self._config.set(self._config.token, self._token)
            return {"status": True, **response.json()}
        else:
            return {"status": False, **response.json()}

    def registration(self, login: str, password: str, full_name=None) -> Optional[dict]:
        host_url = self.get_host_url()
        request_url = host_url + "/users/registration"
        data = {
            "username": login,
            "password": password,
            "full_name": full_name
        }
        response = requests.post(request_url, json=data)
        if response.status_code == 200:
            return {"status": True, **response.json()}
        else:
            return {"status": False, **response.json()}