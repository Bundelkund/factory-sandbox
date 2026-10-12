import unittest
from pathlib import Path

class TestTriage(unittest.TestCase):
    def test_ak1_triage_gruen(self):
        """AK1: Die Datei triage.txt enthaelt genau die Zeile 'triage gruen'."""
        triage_file = Path("triage.txt")
        self.assertTrue(triage_file.exists(), "Datei triage.txt existiert nicht.")
        
        inhalt = triage_file.read_text()
        erwartet = "triage gruen"
        
        # Entferne moeglichen abschliessenden Zeilenumbruch fuer Vergleich
        self.assertEqual(inhalt.rstrip("\n"), erwartet, 
                         f"Inhalt von triage.txt ist '{inhalt.rstrip(chr(10))}', erwartet '{erwartet}'.")
