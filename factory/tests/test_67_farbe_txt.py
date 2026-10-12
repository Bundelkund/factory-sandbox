import unittest
import os

class TestIssue67FarbeTxt(unittest.TestCase):
    def test_ak1_farbe_txt_existiert(self):
        """AK1: Die Datei farbe.txt existiert im Repo-Wurzelverzeichnis."""
        self.assertTrue(os.path.isfile('farbe.txt'), "Die Datei farbe.txt existiert nicht im Repo-Wurzelverzeichnis.")

    def test_ak2_farbe_txt_inhalt_ist_blau(self):
        """AK2: Der Inhalt von farbe.txt ist nach Entfernen von fuehrendem und abschliessendem Leerraum genau die Zeichenkette blau."""
        with open('farbe.txt', 'r', encoding='utf-8') as f:
            inhalt = f.read()
        self.assertEqual(inhalt.strip(), 'blau', f"Der Inhalt von farbe.txt ist '{inhalt.strip()}', erwartet wurde 'blau'.")

if __name__ == '__main__':
    unittest.main()
