"""Les tests de la leçon 4. Tu n'as pas à modifier ce fichier."""

import unittest

from exercice import (ajouter_course, appliquer, premier_superieur, repeter,
                      statistiques)


class TestRepeter(unittest.TestCase):
    def test_par_defaut(self):
        self.assertEqual(repeter("ha"), "ha ha")

    def test_nombre_choisi(self):
        self.assertEqual(repeter("ha", 3), "ha ha ha")

    def test_separateur_choisi(self):
        self.assertEqual(repeter("ha", 3, "-"), "ha-ha-ha")

    def test_une_seule_fois(self):
        self.assertEqual(repeter("ha", 1), "ha")


class TestPremierSuperieur(unittest.TestCase):
    def test_trouve(self):
        self.assertEqual(premier_superieur([1, 5, 9], 4), 5)

    def test_absent(self):
        self.assertIsNone(premier_superieur([1, 2], 10))

    def test_liste_vide(self):
        self.assertIsNone(premier_superieur([], 0))

    def test_strictement(self):
        self.assertIsNone(premier_superieur([4, 4], 4))


class TestAppliquer(unittest.TestCase):
    def test_avec_len(self):
        self.assertEqual(appliquer(len, ["a", "bb"]), [1, 2])

    def test_avec_une_lambda(self):
        self.assertEqual(appliquer(lambda n: n * 2, [1, 2, 3]), [2, 4, 6])

    def test_liste_vide(self):
        self.assertEqual(appliquer(len, []), [])


class TestAjouterCourse(unittest.TestCase):
    def test_nouvelle_liste(self):
        self.assertEqual(ajouter_course("pain"), ["pain"])

    def test_liste_existante(self):
        self.assertEqual(ajouter_course("lait", ["pain"]), ["pain", "lait"])

    def test_pas_de_partage_entre_appels(self):
        premiere = ajouter_course("pain")
        seconde = ajouter_course("lait")
        self.assertEqual(premiere, ["pain"])
        self.assertEqual(seconde, ["lait"])


class TestStatistiques(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(statistiques([2, 4, 9]), (2, 9, 5.0))

    def test_un_element(self):
        self.assertEqual(statistiques([7]), (7, 7, 7.0))

    def test_liste_vide(self):
        self.assertEqual(statistiques([]), (None, None, 0.0))


if __name__ == "__main__":
    unittest.main()
