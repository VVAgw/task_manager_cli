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


# класс вызывающий
class CommandInvoker():
    def __init__(self):
        self.cmd = ''

    def set_command(self, command:Command):
        self.cmd = command

    def execute_command(self):
        self.cmd.execute()
    
# Главная функция
def main():
    tsk = TaskStoreAge()
    inv = CommandInvoker()
    addtsk = AddTaskCommand(tsk, "parapapa")
    addts2 = AddTaskCommand(tsk, "22222parapapa")
    addts3 = AddTaskCommand(tsk, "33333parapapa")
    inv.set_command(addtsk)
    inv.execute_command()
    inv.set_command(addts2)
    inv.execute_command()
    inv.set_command(addts3)
    inv.execute_command()

    show_list = ListTasksCommand(tsk)
    inv.set_command(show_list)
    inv.execute_command()

if __name__ == "__main__":
    main()
