import unittest
from pathlib import Path

class TestCanaryNacht2(unittest.TestCase):
    def setUp(self):
        # Stelle sicher, dass das Repo-Wurzelverzeichnis im sys.path steht
        if str(Path.cwd()) not in __import__('sys').path:
            __import__('sys').path.insert(0, str(Path.cwd()))

    def test_ak1_eins_txt_inhalt(self):
        """AK1: Der Inhalt von canary/nacht-2/eins.txt ohne abschliessende Zeilenumbrueche ist genau 'eins'."""
        p = Path('canary/nacht-2/eins.txt')
        self.assertTrue(p.exists(), f"Datei {p} existiert nicht.")
        inhalt = p.read_text(encoding='utf-8').rstrip('\n')
        self.assertEqual(inhalt, 'eins', f"Inhalt von {p} ist '{inhalt}', erwartet 'eins'.")

    def test_ak2_zwei_txt_inhalt(self):
        """AK2: Der Inhalt von canary/nacht-2/zwei.txt ohne abschliessende Zeilenumbrueche ist genau 'zwei'."""
        p = Path('canary/nacht-2/zwei.txt')
        self.assertTrue(p.exists(), f"Datei {p} existiert nicht.")
        inhalt = p.read_text(encoding='utf-8').rstrip('\n')
        self.assertEqual(inhalt, 'zwei', f"Inhalt von {p} ist '{inhalt}', erwartet 'zwei'.")
