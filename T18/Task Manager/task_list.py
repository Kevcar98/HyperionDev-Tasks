class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                return True
        return False

    def display_tasks(self):
        if not self.tasks:
            return "No tasks found."
        else:
            tasks_info = ""
            for task in self.tasks:
                tasks_info += str(task) + "\n"
            return tasks_info
