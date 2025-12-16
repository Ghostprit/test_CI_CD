import unittest
from app import greet

class TestApp(unittest.TestCase):

    def test_greet_world(self):
        """Test that the default greeting works."""
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_name(self):
        """Test a personalized greeting."""
        self.assertEqual(greet("GitHub Actions"), "Hello, GitHub Actions!")

if __name__ == '__main__':
    unittest.main()