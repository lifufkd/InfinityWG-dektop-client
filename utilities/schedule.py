##########################
#       Created By       #
#          SBR           #
##########################
import time

from PySide6.QtCore import QTimer, QThread, QObject, Signal
##########################

##########################


class TaskRunner(QObject):
    finished = Signal()

    def __init__(self, task, interval=None):
        super().__init__()
        self.task = task
        self.interval = interval

    def run(self):
        if self.interval:
            while True:
                self.task()
                time.sleep(self.interval/1000)
        else:
            self.task()


class TaskScheduler:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, task, interval=None):
        """
        Add a new task to the scheduler.

        Parameters:
            task_name (str): Unique name for the task.
            task (function): The task function to be executed.
            interval (int): The interval in milliseconds at which the task should repeat. If None, the task runs only once.
        """
        if task_name in self.tasks:
            raise ValueError("Task with this name already exists.")

        thread = QThread()
        runner = TaskRunner(task, interval)
        runner.moveToThread(thread)

        runner.finished.connect(thread.quit)
        runner.finished.connect(runner.deleteLater)
        thread.finished.connect(thread.deleteLater)

        thread.started.connect(runner.run)
        thread.start()

        self.tasks[task_name] = (thread, runner)

    def stop_task(self, task_name):
        """
        Remove a task from the scheduler.

        Parameters:
            task_name (str): The name of the task to remove.
        """
        if task_name in self.tasks:
            thread, runner = self.tasks.pop(task_name)
            thread.quit()
            thread.wait()
