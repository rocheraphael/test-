"""Les tests de la leçon 3. Tu n'as pas à modifier ce fichier."""

import unittest

from exercice import compter, inverser, maximum, moyenne, pairs, somme


class TestSomme(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(somme([1, 2, 3]), 6)

    def test_liste_vide(self):
        self.assertEqual(somme([]), 0)

    def test_negatifs(self):
        self.assertEqual(somme([-1, 1, -2]), -2)


class TestMaximum(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(maximum([12, 15, 8]), 15)

    def test_que_des_negatifs(self):
        self.assertEqual(maximum([-5, -2, -9]), -2)

    def test_un_seul_element(self):
        self.assertEqual(maximum([42]), 42)

    def test_liste_vide(self):
        with self.assertRaises(ValueError):
            maximum([])


class TestMoyenne(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(moyenne([10, 20]), 15.0)

    def test_arrondi(self):
        self.assertEqual(moyenne([12, 15, 8, 19]), 13.5)
        self.assertEqual(moyenne([1, 2]), 1.5)

    def test_liste_vide(self):
        self.assertEqual(moyenne([]), 0.0)


class TestPairs(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(pairs([1, 2, 3, 4]), [2, 4])

    def test_aucun_pair(self):
        self.assertEqual(pairs([1, 3]), [])

    def test_ne_modifie_pas_l_original(self):
        original = [1, 2, 3, 4]
        pairs(original)
        self.assertEqual(original, [1, 2, 3, 4])


class TestCompter(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(compter([1, 5, 9], 4), 2)

    def test_strictement_superieur(self):
        self.assertEqual(compter([4, 4, 4], 4), 0)

    def test_liste_vide(self):
        self.assertEqual(compter([], 0), 0)


class TestInverser(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(inverser([1, 2, 3]), [3, 2, 1])

    def test_liste_vide(self):
        self.assertEqual(inverser([]), [])

    def test_ne_modifie_pas_l_original(self):
        original = [1, 2, 3]
        inverser(original)
        self.assertEqual(original, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
