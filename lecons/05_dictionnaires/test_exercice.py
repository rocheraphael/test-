"""Les tests de la leçon 5. Tu n'as pas à modifier ce fichier."""

import unittest

from exercice import (compter_mots, fusionner_stocks, inverser_dictionnaire,
                      mot_le_plus_frequent, moyenne_par_eleve,
                      regrouper_par_initiale)


class TestCompterMots(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(compter_mots("le chat le"), {"le": 2, "chat": 1})

    def test_casse_ignoree(self):
        self.assertEqual(compter_mots("Le le LE"), {"le": 3})

    def test_texte_vide(self):
        self.assertEqual(compter_mots(""), {})


class TestMotLePlusFrequent(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(mot_le_plus_frequent("le chat le chien le"), "le")

    def test_egalite_premier_rencontre(self):
        self.assertEqual(mot_le_plus_frequent("chat chien"), "chat")

    def test_texte_vide(self):
        self.assertIsNone(mot_le_plus_frequent(""))


class TestInverserDictionnaire(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(inverser_dictionnaire({"a": 1, "b": 2}), {1: "a", 2: "b"})

    def test_vide(self):
        self.assertEqual(inverser_dictionnaire({}), {})

    def test_valeurs_en_double(self):
        self.assertEqual(inverser_dictionnaire({"a": 1, "b": 1}), {1: "b"})


class TestFusionnerStocks(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(
            fusionner_stocks({"pomme": 3}, {"pomme": 2, "poire": 1}),
            {"pomme": 5, "poire": 1},
        )

    def test_un_vide(self):
        self.assertEqual(fusionner_stocks({}, {"poire": 1}), {"poire": 1})

    def test_ne_modifie_pas_les_originaux(self):
        a = {"pomme": 3}
        b = {"pomme": 2}
        fusionner_stocks(a, b)
        self.assertEqual(a, {"pomme": 3})
        self.assertEqual(b, {"pomme": 2})


class TestRegrouperParInitiale(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(
            regrouper_par_initiale(["chat", "chien", "loup"]),
            {"c": ["chat", "chien"], "l": ["loup"]},
        )

    def test_casse(self):
        self.assertEqual(regrouper_par_initiale(["Chat"]), {"c": ["Chat"]})

    def test_liste_vide(self):
        self.assertEqual(regrouper_par_initiale([]), {})


class TestMoyenneParEleve(unittest.TestCase):
    def test_cas_simple(self):
        self.assertEqual(
            moyenne_par_eleve({"Alice": [15, 17], "Bob": [10, 11, 12]}),
            {"Alice": 16.0, "Bob": 11.0},
        )

    def test_sans_note(self):
        self.assertEqual(moyenne_par_eleve({"Alice": []}), {"Alice": 0.0})

    def test_vide(self):
        self.assertEqual(moyenne_par_eleve({}), {})


if __name__ == "__main__":
    unittest.main()
