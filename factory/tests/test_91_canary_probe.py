import os
import unittest


class TestCanaryProbe(unittest.TestCase):
    def test_ak1_datei_existiert(self):
        self.assertTrue(os.path.isfile('canary/probe-2026-10-14/hallo.txt'))

    def test_ak2_inhalt_ist_korrekt(self):
        with open('canary/probe-2026-10-14/hallo.txt', encoding='utf-8') as f:
            inhalt = f.read().rstrip('\n')
        self.assertEqual(inhalt, 'Guten Morgen, Factory')
