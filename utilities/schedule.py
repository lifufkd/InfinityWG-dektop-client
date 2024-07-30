##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtCore import QTimer
##########################

##########################


class TaskScheduler:
    def __init__(self):
        self._tasks = dict()

    def add_task(self, task: object, timeout: int) -> None:
        timer = QTimer()
        timer.timeout.connect(task)
        timer.start(timeout)
        self._tasks.update({task: timer})

    def stop_task(self, task: object) -> None:
        self._tasks.pop(task).stop()