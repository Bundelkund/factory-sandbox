import unittest
from pathlib import Path

class TestGateTxt(unittest.TestCase):
    def test_ak1_gate_txt_inhalt(self):
        """AK1: Die Datei gate.txt enthaelt genau die Zeile 'gate gruen'."""
        repo_root = Path.cwd()
        gate_file = repo_root / "gate.txt"
        
        self.assertTrue(gate_file.exists(), "Die Datei gate.txt existiert nicht.")
        
        inhalt = gate_file.read_text()
        erwartet = "gate gruen"
        
        # Entferne moeglichen abschliessenden Zeilenumbruch fuer Vergleich
        inhalt_ohne_leerzeilen = inhalt.rstrip("\n")
        
        self.assertEqual(inhalt_ohne_leerzeilen, erwartet,
                         f"gate.txt enthaelt nicht genau 'gate gruen', sondern: '{inhalt_ohne_leerzeilen}'")
