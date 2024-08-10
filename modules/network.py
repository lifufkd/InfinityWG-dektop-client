##########################
#       Created By       #
#          SBR           #
##########################
import time
import psutil
from ping3 import ping
import requests
import socket
##########################

##########################


def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
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


def check_ping(domain, duration=5):
    start_time = time.time()
    pings = []

    while time.time() - start_time < duration:
        ping_time = ping(domain, timeout=5)
        if ping_time is not None:
            pings.append(ping_time * 1000)

        time.sleep(1)

    if pings:
        average_ping = sum(pings) / len(pings)
        if average_ping == 0.0:
            return None
        return average_ping
    else:
        return None


def check_internet_and_dns(hosts: str, duration: int = 5) -> bool:
    ping_servers = list()
    test_urls = list()
    test_domains = list()

    for host in hosts:
        ping_servers.append(host[0])
        test_domains.append(host[1])
        test_urls.append("https://" + host[1])

    # Проверка пинга
    ping_success = any(check_ping(server, duration) for server in ping_servers)
    if ping_success:
        ping_status = True
    else:
        ping_status = False


    # Проверка HTTP/HTTPS соединения
    http_success = False
    for url in test_urls:
        try:
            response = requests.get(url, timeout=duration)
            if response.status_code == 200:
                http_success = True
                break
        except requests.RequestException as e:
            continue
    if http_success:
        http_status = True
    else:
        http_status = False

    # Проверка разрешения DNS
    dns_success = False
    for domain in test_domains:
        try:
            socket.gethostbyname(domain)
            dns_success = True
            break
        except socket.error as e:
            continue
    if dns_success:
        dns_status = True
    else:
        dns_status = False

    if ping_status and http_status and dns_status:
        return True
    else:
        return False


def get_network_speed(interval: int = 1) -> dict:
    try:
        io_object = psutil.net_io_counters()
        bytes_sent_start = io_object.bytes_sent
        bytes_received_start = io_object.bytes_recv

        time.sleep(interval)

        final_data = psutil.net_io_counters()
        final_bytes_sent = final_data.bytes_sent
        final_bytes_recv = final_data.bytes_recv

        bytes_sent_avg = (final_bytes_sent - bytes_sent_start) / interval
        bytes_recv_avg = (final_bytes_recv - bytes_received_start) / interval
    except Exception as e:
        return {"status": False, "detail": str(e)}

    return {"status": True, "bytes_sent": bytes_sent_avg, "bytes_recv": bytes_recv_avg}
