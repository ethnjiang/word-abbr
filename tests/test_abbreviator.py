import unittest

from word_abbr.abbreviator import Abbreviator


class TestAbbreviator(unittest.TestCase):
    def setUp(self):
        self.abbrev = Abbreviator()

    def test_internal_abbreviation(self):
        self.assertEqual(self.abbrev.get("doctor"), "Dr.")
        self.assertEqual(self.abbrev.get("professor"), "Prof.")

    def test_data_file_abbreviation(self):
        self.assertEqual(self.abbrev.get("university"), "uni")  # 来自 abbreviations.json
        self.assertEqual(self.abbrev.get("application"), "app")

    def test_generic_fallback(self):
        abbr = self.abbrev.get("overdue")
        self.assertEqual(abbr, "ovd")

    def test_get_full_info(self):
        info = self.abbrev.get_full_info("doctor")
        self.assertEqual(info["abbr"], "Dr.")
        self.assertEqual(info["source"], "internal")

        info = self.abbrev.get_full_info("university")
        self.assertEqual(info["abbr"], "uni")
        self.assertEqual(info["source"], "data_file")
        #
        # info = self.abbrev.get_full_info("unknownword")
        # self.assertNotEqual(info["abbr"], "unknownword")
        # self.assertEqual(info["source"], "generic_algorithm")


if __name__ == "__main__":
    unittest.main()