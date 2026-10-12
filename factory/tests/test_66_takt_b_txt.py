import unittest
from pathlib import Path

class TestTaktB(unittest.TestCase):
    def test_ak1_dateiinhalt(self):
        """AK1: Die Datei takt-b.txt enthaelt genau den Text 'Takt B' (ein Zeilenumbruch am Ende ist erlaubt)."""
        expected = "Takt B"
        actual = Path("takt-b.txt").read_text().rstrip("\n")
        self.assertEqual(actual, expected, f"Dateiinhalt von takt-b.txt ist '{actual}', erwartet '{expected}'")

