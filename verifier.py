#!/usr/bin/env python3
"""Vérifie tes exercices.

    python3 verifier.py        -> toutes les leçons
    python3 verifier.py 03     -> seulement la leçon 03
    python3 verifier.py 03 -v  -> et affiche le détail des erreurs
"""

import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).parent
DOSSIER_LECONS = RACINE / "lecons"

# Les couleurs ne s'affichent pas partout (vieux terminal Windows, sortie
# redirigée vers un fichier). On les désactive plutôt que d'afficher des
# caractères bizarres.
if sys.stdout.isatty():
    VERT = "\033[32m"
    ROUGE = "\033[31m"
    GRIS = "\033[90m"
    GRAS = "\033[1m"
    FIN = "\033[0m"
else:
    VERT = ROUGE = GRIS = GRAS = FIN = ""


def lecons(filtre=None):
    """Retourne les dossiers de leçons, triés, éventuellement filtrés."""
    tous = sorted(d for d in DOSSIER_LECONS.iterdir() if d.is_dir())
    if filtre is None:
        return tous
    return [d for d in tous if d.name.startswith(filtre)]


def verifier(dossier, bavard=False):
    """Lance les tests d'une leçon. Retourne True si tout passe."""
    resultat = subprocess.run(
        [sys.executable, "-m", "unittest", "test_exercice", "-q"],
        cwd=dossier,
        capture_output=True,
        text=True,
    )
    reussi = resultat.returncode == 0
    etat = f"{VERT}OK{FIN}" if reussi else f"{ROUGE}à faire{FIN}"
    print(f"  {dossier.name:<24} {etat}")
    if not reussi and bavard:
        print(GRIS + resultat.stderr.rstrip() + FIN)
    return reussi


def main():
    arguments = [a for a in sys.argv[1:] if a not in ("-v", "--verbose")]
    bavard = len(arguments) != len(sys.argv[1:])
    filtre = arguments[0] if arguments else None

    a_verifier = lecons(filtre)
    if not a_verifier:
        print(f"Aucune leçon ne correspond à « {filtre} ».")
        return 1

    print(f"\n{GRAS}Où tu en es{FIN}\n")
    resultats = [verifier(d, bavard) for d in a_verifier]
    faits = sum(resultats)
    total = len(resultats)
    print(f"\n{faits}/{total} leçons terminées.")

    if faits < total:
        prochaine = a_verifier[resultats.index(False)].name
        print(f"Prochaine étape : {GRAS}lecons/{prochaine}/lecon.md{FIN}")
        if not bavard:
            print(f"{GRIS}Astuce : ajoute -v pour voir le détail des erreurs.{FIN}")
    else:
        print("Tout est vert. Direction projet/README.md.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
