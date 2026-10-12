import unittest
from pathlib import Path

class TestCiTxt(unittest.TestCase):
    def test_ak1_ci_txt_inhalt(self):
        """AK1: Die Datei ci.txt enthaelt genau die Zeile 'ci rot'."""
        ci_file = Path("ci.txt")
        self.assertTrue(ci_file.exists(), "Die Datei ci.txt existiert nicht.")
        inhalt = ci_file.read_text()
        erwartet = "ci rot"
        # Entferne moeglichen abschliessenden Zeilenumbruch fuer den Vergleich
        self.assertEqual(inhalt.rstrip("\n"), erwartet,
                         f"Inhalt von ci.txt ist '{inhalt.rstrip(chr(10))}', erwartet '{erwartet}'")
