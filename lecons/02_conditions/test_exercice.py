"""Les tests de la leçon 2. Tu n'as pas à modifier ce fichier."""

import unittest

from exercice import est_bissextile, mention, signe, tarif


class TestMention(unittest.TestCase):
    def test_tres_bien(self):
        self.assertEqual(mention(18), "Très bien")
        self.assertEqual(mention(16), "Très bien")

    def test_bien(self):
        self.assertEqual(mention(15), "Bien")
        self.assertEqual(mention(14), "Bien")

    def test_passable(self):
        self.assertEqual(mention(12), "Passable")
        self.assertEqual(mention(10), "Passable")

    def test_insuffisant(self):
        self.assertEqual(mention(9), "Insuffisant")
        self.assertEqual(mention(0), "Insuffisant")

    def test_bornes(self):
        self.assertEqual(mention(20), "Très bien")

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            mention(21)
        with self.assertRaises(ValueError):
            mention(-1)


class TestEstBissextile(unittest.TestCase):
    def test_divisible_par_4(self):
        self.assertTrue(est_bissextile(2024))

    def test_annee_ordinaire(self):
        self.assertFalse(est_bissextile(2023))

    def test_siecle_non_bissextile(self):
        self.assertFalse(est_bissextile(1900))

    def test_siecle_bissextile(self):
        self.assertTrue(est_bissextile(2000))


class TestTarif(unittest.TestCase):
    def test_enfant(self):
        self.assertEqual(tarif(10, "lundi"), 6)
        self.assertEqual(tarif(13, "mercredi"), 6)

    def test_mercredi(self):
        self.assertEqual(tarif(30, "mercredi"), 8)

    def test_plein_tarif(self):
        self.assertEqual(tarif(30, "samedi"), 11)
        self.assertEqual(tarif(14, "lundi"), 11)


class TestSigne(unittest.TestCase):
    def test_positif(self):
        self.assertEqual(signe(3), "positif")

    def test_negatif(self):
        self.assertEqual(signe(-3), "négatif")

    def test_nul(self):
        self.assertEqual(signe(0), "nul")


if __name__ == "__main__":
    unittest.main()
