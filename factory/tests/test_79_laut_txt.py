import unittest
from pathlib import Path

class TestIssue79LautTxt(unittest.TestCase):
    def test_ak1_laut_txt_inhalt(self):
        """AK1: Die Datei laut.txt enthaelt genau die Zeile HALLO WELT (nur Grossbuchstaben)."""
        erwartet = 'HALLO WELT'
        actual = Path('laut.txt').read_text().rstrip('\n')
        self.assertEqual(actual, erwartet, f"Inhalt von laut.txt ist '{actual}', erwartet '{erwartet}'")

