##########################
#       Created By       #
#          SBR           #
##########################
from PySide6.QtCore import QTimer, QThread, QObject, Signal, QDateTime
from functools import partial
##########################

##########################


class TaskRunner(QObject):
    finished = Signal()

    def __init__(self, task, interval=None):
        super().__init__()
        self.task = task
        self.interval = interval
        self.timer = None

    def run(self):
        self.task(self.stop)
        if self.interval is not None:
            self.timer = QTimer()
            self.timer.timeout.connect(partial(self.task, self.stop))
            self.timer.start(self.interval)
        else:
            self.stop()

    def stop(self):
        if self.timer:
            self.timer.stop()
        self.finished.emit()


class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, task, start_time=None, interval=None):
        """
        Add a new task to the scheduler.

        Parameters:
            task_name (str): Unique name for the task.
            task (function): The task function to be executed.
            start_time (QDateTime): The start time of the task. If None, execute immediately.
            interval (int): The interval in milliseconds at which the task should repeat. If None, the task runs only once.
        """
        if task_name in self.tasks:
            self.remove_task(task_name=task_name)

        if start_time is None:
            start_time = QDateTime.currentDateTime()

        delay = max(0, int(start_time.toMSecsSinceEpoch() - QDateTime.currentMSecsSinceEpoch()))

        thread = QThread()
        runner = TaskRunner(task, interval)
        runner.moveToThread(thread)

        runner.finished.connect(partial(self.remove_task, task_name))
        runner.finished.connect(thread.quit)
        runner.finished.connect(runner.deleteLater)
        thread.finished.connect(thread.deleteLater)

        thread.started.connect(runner.run)

        if delay > 0:
            timer = QTimer()
            timer.setSingleShot(True)
            timer.timeout.connect(thread.start)
            timer.start(delay)
            self.tasks[task_name] = (thread, runner, timer)
        else:
            thread.start()
            self.tasks[task_name] = (thread, runner)

    def remove_task(self, task_name):
        """
        Remove a task from the scheduler.

        Parameters:
            task_name (str): The name of the task to remove.
        """
        if task_name in self.tasks:
            task_info = self.tasks.pop(task_name)
            thread, runner = task_info[0], task_info[1]
            try:
                if runner.timer:
                    runner.timer.stop()
                if thread.isRunning():
                    thread.quit()
                    thread.wait()
                if len(task_info) > 2:
                    task_info[2].stop()
            except Exception as e:
                return False
        else:
            return False