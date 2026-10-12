import os
import unittest


class TestGrussTxt(unittest.TestCase):
    def test_ak1_gruss_txt_existiert(self):
        """AK1: Die Datei gruss.txt existiert im Repo-Wurzelverzeichnis als regulaere Datei."""
        self.assertTrue(os.path.isfile('gruss.txt'), "Die Datei gruss.txt existiert nicht im Repo-Wurzelverzeichnis.")

    def test_ak2_gruss_txt_inhalt(self):
        """AK2: Der Inhalt von gruss.txt ist nach Entfernen eines abschliessenden Zeilenumbruchs genau 'Hallo Factory'."""
        with open('gruss.txt', 'r', encoding='utf-8') as f:
            inhalt = f.read().rstrip('\n')
        self.assertEqual(inhalt, 'Hallo Factory', f"Der Inhalt von gruss.txt ist '{inhalt}', erwartet wurde 'Hallo Factory'.")
