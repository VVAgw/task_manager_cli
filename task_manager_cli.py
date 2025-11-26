import json
from abc import ABC, abstractmethod

# Класс хранителя
class TaskStoreAge:
    def __init__(self):
        self.tasks = {}
        self.id = 1

    def add_task(self, desc):
        self.tasks[self.id] = desc
        self.id += 1

    def list_tasks(self):
        return self.tasks

# Абстрактный класс, выступает в роли шаблона
class Command(ABC):
    def __init__(self, obj:TaskStoreAge):
        self.obj = obj

    @abstractmethod
    def execute(self):
        pass
 
# Класс добавления задачи
class AddTaskCommand(Command):
    def __init__(self, obj:TaskStoreAge, desc):
        super().__init__(obj)
        self.desc = desc

    def execute(self):
        self.obj.add_task(self.desc)

# Класс вывода списка задачь
class ListTasksCommand(Command):
    def __init__(self, obj:TaskStoreAge):
        super().__init__(obj)

    def execute(self):
        print(self.obj.list_tasks())

