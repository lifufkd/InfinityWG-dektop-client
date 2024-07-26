# coding:utf-8
from qfluentwidgets import (qconfig, QConfig, ConfigItem)


class Config(QConfig):
    """ Config of application """

    # System settings
    token = ConfigItem(
        "System", "token", "")

    host = ConfigItem(
        "System", "host", "http://localhost:8000"
    )


cfg = Config()
qconfig.load('../config.json', cfg)