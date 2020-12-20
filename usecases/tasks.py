from domains import Task
from modules import TasksManager


class Tasks:
    @staticmethod
    def list():
        tasks = TasksManager.query.all()
        return [Task(task.name, task.description, task.id) for task in tasks]

    @staticmethod
    def new(task: Task):
        t = TasksManager(task.name, task.description)
        t.save()
        return Task(t.name, t.description, t.id)
