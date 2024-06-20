import unittest
from task import Task
from user import User
from task_list import TaskList
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()
        self.task_manager.task_lists = {}  # Reset task lists for each test

    def test_create_task_list(self):
        self.task_manager.create_task_list("Work")
        self.assertIn("Work", self.task_manager.task_lists)
        self.assertIsInstance(self.task_manager.task_lists["Work"], TaskList)

    def test_add_task(self):
        self.task_manager.create_task_list("Work")
        self.task_manager.add_task("Work", "Finish report", "High")
        task_list = self.task_manager.task_lists["Work"]
        self.assertEqual(len(task_list.tasks), 1)
        self.assertEqual(task_list.tasks[0].name, "Finish report")
        self.assertEqual(task_list.tasks[0].priority, "High")

    def test_remove_task(self):
        self.task_manager.create_task_list("Work")
        self.task_manager.add_task("Work", "Finish report", "High")
        self.task_manager.remove_task("Work", "Finish report")
        task_list = self.task_manager.task_lists["Work"]
        self.assertEqual(len(task_list.tasks), 0)

    def test_update_task_status(self):
        self.task_manager.create_task_list("Work")
        self.task_manager.add_task("Work", "Finish report", "High")
        self.task_manager.update_task_status("Work", "Finish report")
        task_list = self.task_manager.task_lists["Work"]
        self.assertTrue(task_list.tasks[0].complete)

    def test_assign_user(self):
        self.task_manager.create_task_list("Work")
        self.task_manager.add_task("Work", "Finish report", "High")
        self.task_manager.assign_user("Work", "Finish report", "Max")
        task_list = self.task_manager.task_lists["Work"]
        self.assertEqual(str(task_list.tasks[0].user), "Max")

    def test_display_all_task_lists(self):
        self.task_manager.create_task_list("Work")
        self.task_manager.create_task_list("Personal")
        self.assertIn("Work", self.task_manager.task_lists)
        self.assertIn("Personal", self.task_manager.task_lists)


if __name__ == "__main__":
    unittest.main()
