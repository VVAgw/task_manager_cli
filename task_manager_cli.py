import json

class TaskStore:
    def __init__(self):
        self.tasks = {}
        self.id = 1

    def add_task(self, desc):
        self.tasks[self.id] = desc
        self.id += 1

    def list_tasks(self):
        return self.tasks


