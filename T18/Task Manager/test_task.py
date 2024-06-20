import unittest
from task import Task
from user import User


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task("Finish report", "High")

    def test_initialization(self):
        self.assertEqual(self.task.name, "Finish report")
        self.assertEqual(self.task.priority, "High")
        self.assertFalse(self.task.complete)
        self.assertIsNone(self.task.user)

    def test_toggle_completion(self):
        self.task.toggle_completion()
        self.assertTrue(self.task.complete)
        self.task.toggle_completion()
        self.assertFalse(self.task.complete)

    def test_assign_user(self):
        user = User("Max")
        self.task.assign_user(user)
        self.assertEqual(self.task.user, user)


if __name__ == "__main__":
    unittest.main()
