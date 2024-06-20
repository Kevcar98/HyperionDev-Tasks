import unittest
from user import User


class TestUser(unittest.TestCase):

    def test_user_initialization(self):
        user = User("Max")
        self.assertEqual(user.name, "Max")

    def test_user_str(self):
        user = User("Max")
        self.assertEqual(str(user), "Max")


if __name__ == "__main__":
    unittest.main()
