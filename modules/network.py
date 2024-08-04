##########################
#       Created By       #
#          SBR           #
##########################
import time
from ping3 import ping
import requests
##########################

##########################


def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=1)
        response.raise_for_status()
        ip_address = response.json()['ip']
        return {"status": True, "detail": None, "data": ip_address}
    except requests.RequestException as e:
        return {"status": False, "detail": str(e)}


def get_country_by_ip():
    try:
        response = requests.get('https://ipapi.co/json/', timeout=5)
        data = response.json()
        country = data.get('country_name')
        if country:
            return {"status": True, "detail": None, "data": country}
        else:
            raise Exception('No internet connection')
    except Exception as e:
        return {"status": False, "detail": str(e)}


def json_error_handler(response):
    try:
        answer = {"status": False, "code": 1, **response.json()}
    except Exception as e:
        answer = {"status": False, "code": 1, "detail":
                  f"Error code: {response.status_code}. No additional info is available"}
    return answer


def process_request(response):
    if response.status_code == 200:
        return {"status": True, "code": None, **response.json()}
    elif response.status_code == 401:
        return {"status": False, "code": 0, **response.json()}
    else:
        return json_error_handler(response)


def check_ping(domain, duration):
    start_time = time.time()
    pings = []

    while time.time() - start_time < duration:
        ping_time = ping(domain, timeout=5)
        if ping_time is not None:
            pings.append(ping_time * 1000)  # Конвертируем секунды в миллисекунды

        # Sleep for a short time before the next ping
        time.sleep(1)

    # Calculate the average ping time
    if pings:
        average_ping = sum(pings) / len(pings)
        if average_ping == 0.0:
            return None
        return average_ping
    else:
        return None
