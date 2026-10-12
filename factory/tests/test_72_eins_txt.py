import os
import unittest


class TestIssue72(unittest.TestCase):
    def test_ak1_datei_existiert(self):
        self.assertTrue(os.path.isfile('eins.txt'), 'Die Datei eins.txt existiert nicht im Repository-Wurzelverzeichnis.')

    def test_ak2_inhalt_ist_eins(self):
        with open('eins.txt', encoding='utf-8') as f:
            inhalt = f.read().strip()
        self.assertEqual(inhalt, 'eins', f'Der Inhalt von eins.txt ist nicht "eins", sondern "{inhalt}".')
