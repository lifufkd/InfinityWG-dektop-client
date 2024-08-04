##########################
#       Created By       #
#          SBR           #
##########################
import os
import subprocess
from modules.system import os_type, create_config
##########################

##########################


class WireGuard:
    def __init__(self):
        super().__init__()

    def connect(self, config: str | None = None, path: str = "resources/wireguard/config.conf") -> dict:
        path = (os.getcwd() + "/" + path).replace("\\", "/")
        status = create_config(path=path, config=config)
        if not status["status"]:
            return {"status": False, "detail": status["detail"]}
        if os_type() == "windows":
            status = self.connect_windows(path)
        elif os_type() == "unix":
            status = self.connect_linux_mac(path)
        else:
            status = {"status": False, "detail": "Your OS type is not supported"}
        return status

    def disconnect(self, path: str = "config") -> dict:
        if os_type() == "windows":
            status = self.disconnect_windows(path)
        elif os_type() == "unix":
            status = self.disconnect_linux_mac(path)
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