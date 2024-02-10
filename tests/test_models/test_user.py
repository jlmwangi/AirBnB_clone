import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_user_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

