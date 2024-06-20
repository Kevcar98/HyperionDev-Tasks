import json
from task_list import TaskList
from task import Task
from user import User


class TaskManager:
    def __init__(self):
        self.task_lists = {}  # Dictionary to hold multiple task lists
        self.load_data()

    def create_task_list(self, name):
        if name not in self.task_lists:
            self.task_lists[name] = TaskList()
            print(f"Task list '{name}' created successfully.")
        else:
            print(f"Task list '{name}' already exists.")

    def load_data(self):
        try:
            with open("user_data.txt", "r") as file:
                task_lists_data = json.load(file)
                if isinstance(task_lists_data, dict):
                    for list_name, tasks_data in task_lists_data.items():
                        self.create_task_list(list_name)
                        task_list = self.task_lists[list_name]
                        for task_data in tasks_data:
                            name = task_data["name"]
                            priority = task_data["priority"]
                            complete = task_data["complete"]
                            user_name = task_data.get("user")
                            user = User(user_name) if user_name else None
                            task = Task(name, priority)
                            task.complete = complete
                            task.user = user
                            task_list.add_task(task)
                else:
                    print(
                        "Invalid data format in user_data.txt. Expected a dictionary."
                    )
        except FileNotFoundError:
            pass

    def save_data(self):
        task_lists_data = {}
        for list_name, task_list in self.task_lists.items():
            tasks_data = []
            for task in task_list.tasks:
                task_data = {
                    "name": task.name,
                    "priority": task.priority,
                    "complete": task.complete,
                    "user": str(task.user) if task.user else None,
                }
                tasks_data.append(task_data)
            task_lists_data[list_name] = tasks_data
        with open("user_data.txt", "w") as file:
            json.dump(task_lists_data, file, indent=4)

    def add_task(self, list_name, name, priority):
        if list_name not in self.task_lists:
            print("Task list does not exist.")
            return
        task = Task(name, priority)
        self.task_lists[list_name].add_task(task)
        self.save_data()

    def remove_task(self, list_name, name):
        if list_name not in self.task_lists:
            print("Task list does not exist.")
            return
        if self.task_lists[list_name].remove_task(name):
            self.save_data()
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def update_task_status(self, list_name, name):
        if list_name not in self.task_lists:
            print("Task list does not exist.")
            return
        for task in self.task_lists[list_name].tasks:
            if task.name == name:
                task.toggle_completion()
                self.save_data()
                print("Task status updated successfully.")
                return
        print("Task not found.")

    def assign_user(self, list_name, name, user_name):
        if list_name not in self.task_lists:
            print("Task list does not exist.")
            return
        user = User(user_name)
        for task in self.task_lists[list_name].tasks:
            if task.name == name:
                task.assign_user(user)
                self.save_data()
                print(f"User '{user_name}' assigned to task successfully.")
                return
        print("Task not found.")

    def display_tasks(self, list_name):
        if list_name not in self.task_lists:
            print("Task list does not exist.")
            return
        print(self.task_lists[list_name].display_tasks())

    def display_all_task_lists(self):
        if not self.task_lists:
            print("No task lists available.")
        else:
            print("Available task lists:")
            for list_name in self.task_lists:
                print(f"- {list_name}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager\n")
        print("1. Create Task List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Toggle Task Completion Status")
        print("5. Assign User to Task")
        print("6. Display Tasks")
        print("7. Display All Task Lists")
        print("8. Exit\n")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            list_name = input("Enter task list name: ")
            task_manager.create_task_list(list_name)
        elif choice == "2":
            list_name = input("Enter task list name: ")
            name = input("Enter task: ")
            priority = input("Enter task priority: ")
            task_manager.add_task(list_name, name, priority)
        elif choice == "3":
            list_name = input("Enter task list name: ")
            task_name = input("Enter task to remove: ")
            task_manager.remove_task(list_name, task_name)
        elif choice == "4":
            list_name = input("Enter task list name: ")
            task_name = input("Enter task to toggle completion status: ")
            task_manager.update_task_status(list_name, task_name)
        elif choice == "5":
            list_name = input("Enter task list name: ")
            task_name = input("Enter task to assign user: ")
            user_name = input("Enter user name: ")
            task_manager.assign_user(list_name, task_name, user_name)
        elif choice == "6":
            list_name = input("Enter task list name: ")
            task_manager.display_tasks(list_name)
        elif choice == "7":
            task_manager.display_all_task_lists()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
