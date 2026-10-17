import unittest
from pathlib import Path

class TestIssue97(unittest.TestCase):
    def test_ak1_10_zeilen(self):
        """AK1: Die Datei canary/nacht-3/zahlen.txt hat genau 10 Zeilen."""
        datei = Path('canary/nacht-3/zahlen.txt')
        self.assertTrue(datei.exists(), "Datei canary/nacht-3/zahlen.txt fehlt")
        zeilen = datei.read_text(encoding='utf-8').splitlines()
        self.assertEqual(len(zeilen), 10, f"Erwartet 10 Zeilen, erhalten {len(zeilen)}")

    def test_ak2_reihenfolge_1_bis_10(self):
        """AK2: Die Zeilen lauten der Reihe nach 1, 2, ... bis 10."""
        datei = Path('canary/nacht-3/zahlen.txt')
        self.assertTrue(datei.exists(), "Datei canary/nacht-3/zahlen.txt fehlt")
        erwartet = [str(k) for k in range(1, 11)]
        actual = datei.read_text(encoding='utf-8').splitlines()
        self.assertEqual(actual, erwartet, f"Erwartet {erwartet}, erhalten {actual}")
