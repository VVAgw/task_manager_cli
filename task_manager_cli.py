import json
from abc import ABC, abstractmethod

#####----->1   Класс хранителя
class TaskStoreAge:
    def __init__(self):
        self.tasks = {}
        self.id = 1

    def add_task(self, desc):
        self.tasks[self.id] = desc
        self.id += 1

    def list_tasks(self):
        return self.tasks

    def complete_task(self,task_id):
        del_task = self.tasks.pop(task_id)
        return del_task

    def add_task_with_id(self, task_id, description):
        self.tasks[task_id] = description

#####----->2   Абстрактный класс, выступает в роли шаблона
class Command(ABC):
    def __init__(self, obj:TaskStoreAge):
        self.obj = obj

    @abstractmethod
    def execute(self):
        pass

#####----->3   Задача выполнена 
class CompleteTaskCommand(Command):
    def __init__(self, obj:TaskStoreAge, task_id):
        super().__init__(obj)
        self.task_id = task_id
        self.completed_description = ''
        
    def execute(self):
        res = self.obj.complete_task(self.task_id)
        self.completed_description = res

    def undo(self):
        self.obj.add_task_with_id(self.task_id, self.completed_description)

#####----->4   Класс добавления задачи
class AddTaskCommand(Command):
    def __init__(self, obj:TaskStoreAge, desc):
        super().__init__(obj)
        self.desc = desc

    def execute(self):
        self.obj.add_task(self.desc)

#####----->5   Класс вывода списка задачь
class ListTasksCommand(Command):
    def __init__(self, obj:TaskStoreAge):
        super().__init__(obj)

    def execute(self):
        print(self.obj.list_tasks())


#####----->6   класс вызывающий
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

    deltask = CompleteTaskCommand(tsk, 2)
    inv.set_command(deltask)
    inv.execute_command()

    show_list = ListTasksCommand(tsk)
    inv.set_command(show_list)
    inv.execute_command()

if __name__ == "__main__":
    main()
