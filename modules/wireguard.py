##########################
#       Created By       #
#          SBR           #
##########################
import os
import subprocess
from utilities.system import os_type, create_config
from resources.vars import WG_CONFIGS_NAME, WG_DEFAULT_CONFIG_LOCATION
##########################

##########################


class WireGuard:
    def __init__(self):
        super().__init__()

    def connect(self, config: str | None = None, path: str | None = None,
                config_name: str | None = None) -> dict:
        _os_type = os_type()

        def _get_path():
            if path is None or config_name is None:
                return (os.getcwd() + "/" + WG_DEFAULT_CONFIG_LOCATION + "/" + WG_CONFIGS_NAME + ".conf").replace(
                        "\\", "/")
            else:
                if _os_type == "windows":
                    return config_name
                else:
                    return (path + "/" + config_name).replace(
                            "\\", "/")

        status = create_config(path=_get_path(), config=config)
        if not status["status"]:
            return {"status": False, "detail": status["detail"]}
        if _os_type == "windows":
            status = self.connect_windows(_get_path())
        elif _os_type in ["linux", "darwin"]:
            status = self.connect_linux_mac(_get_path())
        else:
            status = {"status": False, "detail": "Your OS type is not supported"}
        return status

    def disconnect(self, path: str | None = None, config_name: str | None = None) -> dict:
        _os_type = os_type()

        def _get_path():
            if path is None or config_name is None:
                if _os_type == "windows":
                    return WG_CONFIGS_NAME
                else:
                    return (os.getcwd() + "/" + WG_DEFAULT_CONFIG_LOCATION + "/" + WG_CONFIGS_NAME + ".conf").replace(
                            "\\", "/")
            else:
                if _os_type == "windows":
                    return config_name
                else:
                    return (path + "/" + config_name).replace(
                            "\\", "/")

        if _os_type == "windows":
            status = self.disconnect_windows(_get_path())
        elif _os_type in ["linux", "darwin"]:
            status = self.disconnect_linux_mac(_get_path())
        else:
            status = {"status": False, "detail": "Your OS type is not supported"}
        return status

    def connect_windows(self, path: str) -> dict:
        try:
            # Command to add a WireGuard tunnel using the configuration file
            subprocess.run(['wireguard.exe', '/installtunnelservice', path], check=True)
            return {"status": True, "detail": "Successfully connected to WireGuard Tunnel"}
        except subprocess.CalledProcessError as e:
            return {"status": False, "detail": str(e)}

    def disconnect_windows(self, config_file):
        try:
            # Command to remove the WireGuard tunnel
            subprocess.run(['wireguard.exe', '/uninstalltunnelservice', config_file], check=True)
            return {"status": True, "detail": "Successfully disconnected to WireGuard Tunnel"}
        except subprocess.CalledProcessError as e:
            return {"status": False, "detail": str(e)}

    def connect_linux_mac(self, path: str) -> dict:
        try:
            # Bring up the WireGuard interface
            subprocess.run(['wg-quick', 'up', path], check=True)
            return {"status": True, "detail": "Successfully connected to WireGuard Tunnel"}
        except subprocess.CalledProcessError as e:
            return {"status": False, "detail": str(e)}

    def disconnect_linux_mac(self, config_file):
        try:
            subprocess.run(['wg-quick', 'down', config_file], check=True)
            return {"status": True, "detail": "Successfully disconnected to WireGuard Tunnel"}
        except subprocess.CalledProcessError as e:
            return {"status": False, "detail": str(e)}