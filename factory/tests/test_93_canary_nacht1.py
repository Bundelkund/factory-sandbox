import os
import unittest


class TestCanaryNacht1(unittest.TestCase):
    def test_ak1_datei_existiert(self):
        """AK1: Die Datei canary/nacht-1/hallo.txt existiert."""
        self.assertTrue(os.path.isfile('canary/nacht-1/hallo.txt'),
                        'Die Datei canary/nacht-1/hallo.txt existiert nicht.')

    def test_ak2_inhalt_ist_korrekt(self):
        """AK2: Der Inhalt von canary/nacht-1/hallo.txt ohne abschliessende Zeilenumbrueche ist genau 'Guten Morgen, Factory'."""
        with open('canary/nacht-1/hallo.txt', encoding='utf-8') as f:
            inhalt = f.read().rstrip('\n')
        self.assertEqual(inhalt, 'Guten Morgen, Factory',
                         f'Inhalt ist falsch: erwartet "Guten Morgen, Factory", erhalten "{inhalt}"')
