import unittest
from pathlib import Path

class TestNeun(unittest.TestCase):
    def test_ak1_neun_txt_inhalt(self):
        """AK1: Die Datei `neun.txt` enthaelt genau die Zeile `neun`."""
        datei = Path("neun.txt")
        self.assertTrue(datei.exists(), "Datei neun.txt fehlt.")
        inhalt = datei.read_text()
        erwartet = "neun"
        self.assertEqual(inhalt.rstrip("\n"), erwartet, f"Inhalt von neun.txt ist '{inhalt.rstrip(chr(10))}' statt '{erwartet}'.")

