import unittest
from pathlib import Path

class TestIssue65(unittest.TestCase):
    def test_ak1_takt_a_txt_inhalt(self):
        """AK1: Die Datei takt-a.txt enthaelt genau den Text `Takt A` (ein Zeilenumbruch am Ende ist erlaubt)."""
        expected = "Takt A"
        actual = Path("takt-a.txt").read_text().rstrip("\n")
        self.assertEqual(actual, expected, f"Datei takt-a.txt enthaelt '{actual}', erwartet '{expected}'")

