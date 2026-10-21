import subprocess
import sys
import unittest
from pathlib import Path


class TestCanaryNacht4Gruss(unittest.TestCase):
    def setUp(self):
        self.script_path = Path('canary/nacht-4/gruss.sh')

    def test_ak1_hallo_anna(self):
        """AK1: `bash canary/nacht-4/gruss.sh Anna` gibt genau `Hallo, Anna!` mit einem Zeilenumbruch am Ende aus."""
        result = subprocess.run(
            ['bash', str(self.script_path), 'Anna'],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout, 'Hallo, Anna!\n',
                         f"Erwartete Ausgabe 'Hallo, Anna!\n', erhielt '{result.stdout}'")

    def test_ak2_hallo_welt(self):
        """AK2: `bash canary/nacht-4/gruss.sh` ohne Argument gibt genau `Hallo, Welt!` mit einem Zeilenumbruch am Ende aus."""
        result = subprocess.run(
            ['bash', str(self.script_path)],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout, 'Hallo, Welt!\n',
                         f"Erwartete Ausgabe 'Hallo, Welt!\n', erhielt '{result.stdout}'")

    def test_ak3_rueckgabewert_0(self):
        """AK3: Beide Aufrufe enden mit Rueckgabewert 0."""
        returncodes = [
            subprocess.run(
                ['bash', str(self.script_path), *a],
                capture_output=True
            ).returncode
            for a in (['Anna'], [])
        ]
        self.assertEqual(returncodes, [0, 0],
                         f"Erwartete Returncodes [0, 0], erhielt {returncodes}")
