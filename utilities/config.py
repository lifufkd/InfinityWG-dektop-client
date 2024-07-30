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
    token = ConfigItem(
        "System", "token", "")

    host = ConfigItem(
        "System", "host", "http://localhost:8000"
    )

    country = ConfigItem(
        "VPN", "country", "Auto"
    )

    def __init__(self):
        super().__init__()
        self.setup_config()

    def setup_config(self):
        qconfig.load('config.json', self)