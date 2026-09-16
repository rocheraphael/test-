"""Les tests de la leçon 1. Tu n'as pas à modifier ce fichier."""

import unittest

from exercice import celsius_en_fahrenheit, est_pair, presentation, prix_ttc


class TestCelsiusEnFahrenheit(unittest.TestCase):
    def test_eau_bouillante(self):
        self.assertAlmostEqual(celsius_en_fahrenheit(100), 212.0)

    def test_gel(self):
        self.assertAlmostEqual(celsius_en_fahrenheit(0), 32.0)

    def test_negatif(self):
        self.assertAlmostEqual(celsius_en_fahrenheit(-40), -40.0)


class TestPrixTTC(unittest.TestCase):
    def test_taux_simple(self):
        self.assertEqual(prix_ttc(100, 20), 120.0)

    def test_arrondi(self):
        self.assertEqual(prix_ttc(19.99, 5.5), 21.09)

    def test_taux_nul(self):
        self.assertEqual(prix_ttc(50, 0), 50.0)


class TestPresentation(unittest.TestCase):
    def test_phrase_exacte(self):
        self.assertEqual(presentation("Alice", 30), "Alice a 30 ans.")

    def test_autre_personne(self):
        self.assertEqual(presentation("Bob", 7), "Bob a 7 ans.")

    def test_renvoie_bien_une_chaine(self):
        self.assertIsInstance(presentation("Alice", 30), str)


class TestEstPair(unittest.TestCase):
    def test_pair(self):
        self.assertTrue(est_pair(10))

    def test_impair(self):
        self.assertFalse(est_pair(7))

    def test_zero_est_pair(self):
        self.assertTrue(est_pair(0))

    def test_renvoie_un_booleen(self):
        self.assertIsInstance(est_pair(4), bool)


if __name__ == "__main__":
    unittest.main()
