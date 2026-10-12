import unittest
from pathlib import Path

class TestHandTxt(unittest.TestCase):
    def test_ak1_hand_txt_inhalt(self):
        """AK1: Die Datei hand.txt enthaelt genau die Zeile 'von Hand'."""
        expected = "von Hand"
        actual = Path("hand.txt").read_text().rstrip("\n")
        self.assertEqual(actual, expected, f"hand.txt sollte '{expected}' enthalten, aber hat: '{actual}'")
