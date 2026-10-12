import unittest
from pathlib import Path


class TestAchtTxt(unittest.TestCase):
    def test_ak1_acht_txt_inhalt(self):
        """AK1: Die Datei `acht.txt` enthaelt genau die Zeile `acht`."""
        datei = Path("acht.txt")
        self.assertTrue(datei.exists(), "Datei acht.txt existiert nicht.")
        inhalt = datei.read_text()
        erwartet = "acht"
        self.assertEqual(inhalt.rstrip("\n"), erwartet, f"Inhalt von acht.txt ist '{inhalt.rstrip(chr(10))}' statt '{erwartet}'.")

