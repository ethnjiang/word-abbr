import unittest
from unittest.mock import patch
from io import StringIO
from word_abbr.cli import main

class TestCLI(unittest.TestCase):
    @patch('sys.argv', ['word-abbr', 'doctor'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_basic(self, mock_stdout):
        main()
        self.assertEqual(mock_stdout.getvalue().strip(), 'Dr.')

    @patch('sys.argv', ['word-abbr', 'university', '--full'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cli_full(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Word: university", output)

if __name__ == "__main__":
    unittest.main()