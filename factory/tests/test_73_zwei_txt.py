import os
import unittest


class TestIssue73(unittest.TestCase):
    def test_ak1_datei_existiert(self):
        """AK1: Die Datei zwei.txt existiert im Repository-Wurzelverzeichnis."""
        self.assertTrue(os.path.isfile('zwei.txt'), "Die Datei zwei.txt existiert nicht.")

    def test_ak2_inhalt_ist_zwei(self):
        """AK2: Der Inhalt von zwei.txt ist nach Entfernen von umgebendem Leerraum genau das Wort zwei."""
        with open('zwei.txt', encoding='utf-8') as f:
            inhalt = f.read().strip()
        self.assertEqual(inhalt, 'zwei', f"Erwarteter Inhalt 'zwei', aber erhalten: '{inhalt}'")
