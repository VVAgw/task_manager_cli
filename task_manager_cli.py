import json
from abc import ABC, abstractmethod

class TaskStoreAge:
    def __init__(self):
        self.tasks = {}
        self.id = 1

    def add_task(self, desc):
        self.tasks[self.id] = desc
        self.id += 1

    def list_tasks(self):
        return self.tasks

class Command(ABC):
    def __init__(self, obj:TaskStoreAge):
        self.obj = obj

    @abstractmethod
    def execute(self, desc):
        pass
