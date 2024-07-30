##########################
#       Created By       #
#          SBR           #
##########################
import platform
from plyer import notification
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


