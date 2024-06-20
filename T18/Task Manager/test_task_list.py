import unittest
from task import Task
from task_list import TaskList


class TestTaskList(unittest.TestCase):

    def setUp(self):
        self.task_list = TaskList()

    def test_add_task(self):
        task = Task("Finish report", "High")
        self.task_list.add_task(task)
        self.assertIn(task, self.task_list.tasks)

    def test_remove_task(self):
        task = Task("Finish report", "High")
        self.task_list.add_task(task)
        self.task_list.remove_task("Finish report")
        self.assertNotIn(task, self.task_list.tasks)

    def test_display_tasks(self):
        task = Task("Finish report", "High")
        self.task_list.add_task(task)
        display_output = self.task_list.display_tasks()
        expected_output = (
            "Task: Finish report, Priority: High, Complete: False, Assigned to: None\n"
        )
        self.assertEqual(display_output, expected_output)


if __name__ == "__main__":
    unittest.main()
