class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.complete = False
        self.user = None

    def toggle_completion(self):
        self.complete = not self.complete

    def assign_user(self, user):
        self.user = user

    def __str__(self):
        return f"Task: {self.name}, Priority: {self.priority}, Complete: {self.complete}, Assigned to: {self.user}"
