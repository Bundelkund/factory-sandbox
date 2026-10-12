import unittest
from pathlib import Path

class TestF09ResumeProbe(unittest.TestCase):
    def test_ak1_resume_probe(self):
        """AK1: Die Datei `f09/resume-probe.txt` enthaelt genau die Zeile `resume-probe`."""
        expected = "resume-probe"
        file_path = Path("f09/resume-probe.txt")
        
        # Pruefen, ob die Datei existiert
        self.assertTrue(file_path.exists(), f"Datei {file_path} existiert nicht.")
        
        # Inhalt lesen und Zeilenumbruch am Ende entfernen
        actual = file_path.read_text().rstrip("\n")
        
        self.assertEqual(actual, expected, f"Erwarteter Inhalt: '{expected}', tatsaechlicher Inhalt: '{actual}'")

