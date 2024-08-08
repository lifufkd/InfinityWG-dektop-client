##########################
#       Created By       #
#          SBR           #
##########################
from qfluentwidgets import qconfig, QConfig, ConfigItem
##########################

##########################


class Config(QConfig):
    """ Config of application """

    # System settings
    login_width = ConfigItem(
        "UI", "login_width", 1280)

    login_height = ConfigItem(
        "UI", "login_height", 720)

    app_width = ConfigItem(
        "UI", "app_width", 1280)

    app_height = ConfigItem(
        "UI", "app_height", 720)

    token = ConfigItem(
        "System", "token", "")

    host = ConfigItem(
        "System", "host", "http://localhost:8000"
    )

    internet_check = ConfigItem(
        "System", "check_internet_domain", [
            ["8.8.8.8", "www.google.com"],
            ["8.8.4.4", "www.cloudflare.com"]
        ]
    )

    country = ConfigItem(
        "VPN", "country", "Auto"
    )

    is_internet_check = ConfigItem(
        "Modules", "is_internet_check", True
    )

    def __init__(self):
        super().__init__()
        self.setup_config()

    def setup_config(self):
        qconfig.load('config.json', self)