import unittest
import re
import pandas as pd
from utils.process import checkMatch
from utils.data_manipulation import pre_process


class testPreProcess(unittest.TestCase):
    def setUp(self):
        self.regex = "[a-z]{3,10}$"
        pre_process(self.regex)
        self.sr = pd.read_json("dictionary.json", typ='series')

    def test_pre_process(self):
        """
        test length and values of words in dinctionary and check by regex
        """
        for s in self.sr:
            self.assertTrue(3 <= len(s) <= 10)
            self.assertTrue(s.isalpha())

            self.assertTrue(re.match(self.regex, s))

            self.assertFalse(3 > len(s) or len(s) > 10)
            self.assertFalse(s.__contains__("-"))
            self.assertFalse(s.__contains__(" "))


class testCheckMatch(unittest.TestCase):
    def setUp(self) -> None:
        self.grid = [
            "ylpur",
            "comhg",
            "dblae",
            "reysr",
            "dpeek"
        ]

    def test_check_match(self):
        """
        test checkMatch method: returns True if finds the existing words in grids
        and also returns False if a word does not exist
        """
        self.assertTrue(checkMatch(self.grid, "purge"))
        self.assertTrue(checkMatch(self.grid, "eye"))
        self.assertTrue(checkMatch(self.grid, "drey"))
        self.assertTrue(checkMatch(self.grid, "comply"))
        self.assertTrue(checkMatch(self.grid, "ylpurghmocdblaersyerdpeek"))

        self.assertFalse(checkMatch(self.grid, "ylpurghmocdblaersyerdpeeke"))
        self.assertFalse(checkMatch(self.grid, "blaed"))
        self.assertFalse(checkMatch(self.grid, "ylpurcomhgdblaereysrdpeek"))
        self.assertFalse(checkMatch(self.grid, "ylpurcomhgdblaereysrdpeeke"))
