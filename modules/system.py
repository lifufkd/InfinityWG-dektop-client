##########################
#       Created By       #
#          SBR           #
##########################
import platform
from plyer import notification
from modules.network import check_ping
##########################

##########################


def os_type():
    os_name = platform.system()
    if os_name in ['Linux', 'Darwin', 'Windows']:
        return os_name.lower()
    else:
        return "undetected"


def create_config(path: str, config: str | None) -> dict:
    if config is None: return {"status": True}
    try:
        with open(path, "w") as file:
            file.write(config)
        return {"status": True}
    except Exception as e:
        return {"status": False, "detail": str(e)}


def send_notification(title: str, text: str, duration: int = 5) -> dict:
    try:
        notification.notify(
            title=title,
            message=text,
            timeout=duration
        )
        return {"status": True, "detail": "OK"}
    except Exception as e:
        return {"status": False, "detail": str(e)}


def check_best_vpn_server(countries: dict, mode: bool | None = None) -> list[str] | dict:
    temp = dict()
    if mode is None:
        best_vpn_server = list()
        for country, servers in countries["data"].items():
            for server in servers["hosts"]:
                _ping = check_ping(server[0], 1)
                if _ping is not None:
                    temp.update({_ping: server[0]})
        best_server_ping = min(list(temp.keys()))
        best_vpn_server.append(temp[best_server_ping])
        return best_vpn_server
    else:
        best_vpn_servers = dict()
        for country, servers in countries["data"].items():
            best_vpn_servers[servers["name"]] = list()
            for server in servers["hosts"]:
                _ping = check_ping(server[0], 1)
                if _ping is not None:
                    best_vpn_servers[servers["name"]].append([
                        *server,
                        _ping
                    ])
        return best_vpn_servers




