# test_textgen.py
"""
Tests for TextGen module.
"""

import unittest
from textgen import TextGen

class TestTextGen(unittest.TestCase):
    """Test cases for TextGen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TextGen()
        self.assertIsInstance(instance, TextGen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TextGen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
