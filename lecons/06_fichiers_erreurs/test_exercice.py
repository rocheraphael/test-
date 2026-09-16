"""Les tests de la leçon 6. Tu n'as pas à modifier ce fichier."""

import tempfile
import unittest
from pathlib import Path

from exercice import (ajouter_note, charger_notes, diviser, ecrire_lignes,
                      lire_lignes)


class BaseFichier(unittest.TestCase):
    """Fabrique un dossier temporaire, nettoyé après chaque test."""

    def setUp(self):
        self._dossier = tempfile.TemporaryDirectory()
        self.dossier = Path(self._dossier.name)
        self.chemin = self.dossier / "donnees.txt"

    def tearDown(self):
        self._dossier.cleanup()

    def ecrire(self, contenu):
        self.chemin.write_text(contenu, encoding="utf-8")


class TestLireLignes(BaseFichier):
    def test_lignes_simples(self):
        self.ecrire("pain\nlait\n")
        self.assertEqual(lire_lignes(self.chemin), ["pain", "lait"])

    def test_lignes_vides_ignorees(self):
        self.ecrire("pain\n\n\nlait\n")
        self.assertEqual(lire_lignes(self.chemin), ["pain", "lait"])

    def test_sauts_de_ligne_retires(self):
        self.ecrire("pain\n")
        self.assertEqual(lire_lignes(self.chemin), ["pain"])

    def test_fichier_absent(self):
        self.assertEqual(lire_lignes(self.dossier / "nulle_part.txt"), [])


class TestEcrireLignes(BaseFichier):
    def test_ecriture(self):
        ecrire_lignes(self.chemin, ["a", "b"])
        self.assertEqual(self.chemin.read_text(encoding="utf-8"), "a\nb\n")

    def test_ecrase_le_precedent(self):
        self.ecrire("ancien contenu\n")
        ecrire_lignes(self.chemin, ["neuf"])
        self.assertEqual(self.chemin.read_text(encoding="utf-8"), "neuf\n")

    def test_accents(self):
        ecrire_lignes(self.chemin, ["Chloé"])
        self.assertEqual(self.chemin.read_text(encoding="utf-8"), "Chloé\n")


class TestChargerNotes(BaseFichier):
    def test_cas_simple(self):
        self.ecrire("Alice;15\nBob;12\n")
        self.assertEqual(charger_notes(self.chemin), {"Alice": 15, "Bob": 12})

    def test_espaces_et_lignes_vides(self):
        self.ecrire("  Alice ;15\n\nBob;12\n")
        self.assertEqual(charger_notes(self.chemin), {"Alice": 15, "Bob": 12})

    def test_lignes_abimees_ignorees(self):
        self.ecrire("Alice;15\nn_importe_quoi\nBob;douze\nChloé;18\n")
        self.assertEqual(charger_notes(self.chemin), {"Alice": 15, "Chloé": 18})

    def test_fichier_absent(self):
        self.assertEqual(charger_notes(self.dossier / "nulle_part.txt"), {})


class TestAjouterNote(BaseFichier):
    def test_ajoute_sans_ecraser(self):
        self.ecrire("Alice;15\n")
        ajouter_note(self.chemin, "Bob", 12)
        self.assertEqual(charger_notes(self.chemin), {"Alice": 15, "Bob": 12})

    def test_cree_le_fichier_au_besoin(self):
        ajouter_note(self.chemin, "Alice", 15)
        self.assertEqual(charger_notes(self.chemin), {"Alice": 15})

    def test_note_invalide(self):
        self.ecrire("Alice;15\n")
        with self.assertRaises(ValueError):
            ajouter_note(self.chemin, "Bob", 21)
        # Rien ne doit avoir été écrit.
        self.assertEqual(charger_notes(self.chemin), {"Alice": 15})


class TestDiviser(unittest.TestCase):
    def test_division_normale(self):
        self.assertEqual(diviser(10, 2), 5.0)

    def test_division_par_zero(self):
        self.assertIsNone(diviser(10, 0))


if __name__ == "__main__":
    unittest.main()
