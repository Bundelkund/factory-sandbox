import unittest
from pathlib import Path

class TestCanaryNacht7DateiA(unittest.TestCase):
    def test_ak1_inhalt(self):
        """AK1: Der Inhalt von `canary/nacht-7/datei-a.txt` ohne abschliessende Zeilenumbrueche ist genau `a`."""
        dateipfad = Path('canary/nacht-7/datei-a.txt')
        inhalt = dateipfad.read_text(encoding='utf-8').rstrip('\n')
        self.assertEqual(inhalt, 'a', f"Erwarteter Inhalt 'a', erhalten: '{inhalt}'")
