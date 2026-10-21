import unittest
from pathlib import Path

class TestDateiB(unittest.TestCase):
    def test_ak1_inhalt(self):
        """AK1: Der Inhalt von canary/nacht-7/datei-b.txt ohne abschliessende Zeilenumbrueche ist genau b."""
        datei = Path('canary/nacht-7/datei-b.txt')
        inhalt = datei.read_text(encoding='utf-8').rstrip('\n')
        self.assertEqual(inhalt, 'b', f"Erwarteter Inhalt 'b', erhalten: {repr(inhalt)}")
