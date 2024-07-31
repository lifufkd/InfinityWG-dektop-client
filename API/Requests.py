##########################
#       Created By       #
#          SBR           #
##########################
import requests
from typing import Optional
from utilities.config import Config
from utilities.network import process_request, json_error_handler
##########################

##########################


class Authorization:
    def __init__(self, config: Config):
        super().__init__()
        self.token = config.get(config.token)
        self._config = config

    def get_host_url(self):
        return self._config.get(self._config.host)

    def change_host_url(self, host_url):
        self._config.set(self._config.host, host_url)

    def check_token(self) -> Optional[dict]:
        host_url = self.get_host_url()
        request_url = host_url + "/users/check/token"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        try:
            response = requests.get(request_url, headers=headers)
        except Exception as e:
            return {"status": False, "detail": e}
        return process_request(response=response)

    def login(self, login: str, password: str, remember_me: bool) -> Optional[dict]:
        host_url = self.get_host_url()
        request_url = host_url + "/users/login"
        data = {
            "username": login,
            "password": password
        }
        try:
            response = requests.post(request_url, data=data)
        except Exception as e:
            return {"status": False, "detail": e}
        if response.status_code == 200:
            self.token = response.json()['access_token']
            if remember_me:
                self._config.set(self._config.token, self.token)
            return {"status": True, **response.json()}
        else:
            return json_error_handler(response)

    def registration(self, login: str, password: str, full_name=None) -> Optional[dict]:
        host_url = self.get_host_url()
        request_url = host_url + "/users/registration"
        data = {
            "username": login,
            "password": password,
            "full_name": full_name
        }
        try:
            response = requests.post(request_url, json=data)
        except Exception as e:
            return {"status": False, "detail": e}
        return process_request(response=response)


class VPN:
    def __init__(self, config: Config, authorization: Authorization):
        super().__init__()
        self._config = config
        self._authorization = authorization

    def set_country_config(self, country: str) -> None:
        self._config.set(self._config.country, country)

    def get_country_config(self) -> str:
        return self._config.get(self._config.country)

    def get_country_server(self) -> Optional[dict]:
        host_url = self._authorization.get_host_url()
        request_url = host_url + "/get/countries"
        headers = {
            "Authorization": f"Bearer {self._authorization.token}"
        }
        try:
            response = requests.get(request_url, headers=headers)
        except Exception as e:
            return {"status": False, "detail": e}
        if response.status_code == 200:
            return {"status": True, "data": response.json()}
        else:
            return json_error_handler(response)
