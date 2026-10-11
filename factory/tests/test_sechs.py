import unittest
from pathlib import Path

class TestSechs(unittest.TestCase):
    def test_ak1_sechs_txt_inhalt(self):
        """AK1: Die Datei `sechs.txt` enthaelt genau die Zeile `sechs`."""
        datei = Path("sechs.txt")
        self.assertTrue(datei.exists(), "Die Datei sechs.txt existiert nicht.")
        
        inhalt = datei.read_text()
        erwartet = "sechs"
        
        # Entferne moeglichen abschliessenden Zeilenumbruch fuer Vergleich
        self.assertEqual(inhalt.rstrip("\n"), erwartet, 
                         f"Inhalt von sechs.txt ist '{inhalt.rstrip(chr(10))}', erwartet wurde '{erwartet}'.")
