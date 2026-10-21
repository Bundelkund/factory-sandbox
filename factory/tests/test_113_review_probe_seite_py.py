import subprocess
import sys
import unittest


class TestReviewProbeSeitePy(unittest.TestCase):
    def test_ak1_ueberschrift_gibt_html_zuruck(self):
        """AK1: ueberschrift('Hallo') aus canary/review-probe/seite.py gibt genau <h1>Hallo</h1> zurueck."""
        result = subprocess.run(
            ['python3', '-c',
             "import sys; sys.path.insert(0, 'canary/review-probe'); from seite import ueberschrift; print(ueberschrift('Hallo'), end='')"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout, '<h1>Hallo</h1>',
                         "ueberschrift('Hallo') sollte genau '<h1>Hallo</h1>' zurueckgeben")
