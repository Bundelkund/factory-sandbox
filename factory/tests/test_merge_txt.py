import unittest
from pathlib import Path

class TestMergeTxt(unittest.TestCase):
    def test_ak1_merge_txt_inhalt(self):
        """AK1: Die Datei merge.txt enthaelt genau die Zeile 'merge gruen'."""
        repo_root = Path.cwd()
        merge_file = repo_root / "merge.txt"
        
        self.assertTrue(merge_file.exists(), "Die Datei merge.txt existiert nicht.")
        
        inhalt = merge_file.read_text()
        # Entferne moeglichen abschliessenden Zeilenumbruch fuer den Vergleich
        inhalt_ohne_leerzeilen = inhalt.rstrip("\n")
        
        erwartet = "merge gruen"
        self.assertEqual(inhalt_ohne_leerzeilen, erwartet, 
                         f"Inhalt von merge.txt ist '{inhalt_ohne_leerzeilen}', erwartet wurde '{erwartet}'.")

if __name__ == '__main__':
    unittest.main()
