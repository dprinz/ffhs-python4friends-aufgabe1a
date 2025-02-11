from aufgabe1a import *

import unittest

class TestAufgabe1aMethods(unittest.TestCase):
    def test_arithmetische_mitte(self):
        self.assertEqual(arithmetische_mitte([1,4,10]), 5)
    def test_median_even(self):
        self.assertEqual(median([1,2,5,666]), 3.5)
    def test_median_uneven(self):
        self.assertEqual(median([1, 2, 5]), 2)
    def test_geometrische_mitte(self):
        self.assertAlmostEqual(geometrische_mitte([1,9,81]), 9)
    def test_harmonische_mitte(self):
        self.assertAlmostEqual(harmonische_mitte([4, 6, 12]), 6 )
    def test_modus(self):
        self.assertEqual(modus(['gut', 'mittelprächtig', 'mittelprächtig', 'schlecht']), 'mittelprächtig')
    def test_varianz(self):
        self.assertAlmostEqual(varianz([2, 23, 42, 666]), 77882.69, places = 2)
    def test_standard_abweichung(self):
        self.assertAlmostEqual(standard_abweichung([2, 23, 42, 666]), 279.07, places = 2)
    def test_variationskoeffizient(self):
        self.assertAlmostEqual(variationskoeffizient([2, 23, 42, 666]), 1.52, places = 2)

if __name__ == '__main__':
    unittest.main()

