import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das Repo-Wurzelverzeichnis im sys.path steht
repo_root = Path.cwd()
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))


class TestRechne(unittest.TestCase):
    def test_ak1_import_funktioniert(self):
        """AK1: from rechne import verdopple funktioniert im Repo-Wurzelverzeichnis."""
        try:
            from rechne import verdopple
        except ImportError as e:
            self.fail(f"Import von 'verdopple' aus 'rechne' ist fehlgeschlagen: {e}")

    def test_ak2_verdopple_2_ergibt_4(self):
        """AK2: verdopple(2) ergibt 4."""
        from rechne import verdopple
        ergebnis = verdopple(2)
        self.assertEqual(ergebnis, 4, "verdopple(2) sollte 4 ergeben")

    def test_ak2_verdopple_minus_3_ergibt_minus_6(self):
        """AK2: verdopple(-3) ergibt -6."""
        from rechne import verdopple
        ergebnis = verdopple(-3)
        self.assertEqual(ergebnis, -6, "verdopple(-3) sollte -6 ergeben")

    def test_ak2_verdopple_0_ergibt_0(self):
        """AK2: verdopple(0) ergibt 0."""
        from rechne import verdopple
        ergebnis = verdopple(0)
        self.assertEqual(ergebnis, 0, "verdopple(0) sollte 0 ergeben")
