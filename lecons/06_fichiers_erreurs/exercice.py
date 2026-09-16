"""Leçon 6 — à toi de jouer. Vérifie avec : python3 ../../verifier.py 06

Les fonctions reçoivent un CHEMIN de fichier (une chaîne ou un objet Path).
Ouvre toujours avec `with` et `encoding="utf-8"`.
"""


def lire_lignes(chemin):
    """Renvoie la liste des lignes non vides du fichier, sans saut de ligne.

    Pour un fichier contenant :
        pain
        (ligne vide)
        lait
    la fonction renvoie ["pain", "lait"].

    Si le fichier n'existe pas, renvoie une liste vide (sans planter).
    """
    pass


def ecrire_lignes(chemin, lignes):
    """Écrit chaque élément de `lignes` sur sa propre ligne.

    Écrase le contenu précédent. Chaque ligne se termine par un \\n.
    Ne renvoie rien.
    """
    pass


def charger_notes(chemin):
    """Charge un fichier « nom;note » en dictionnaire {nom: note (int)}.

    Fichier :
        Alice;15
        Bob;12
    Résultat :
        {"Alice": 15, "Bob": 12}

    Les lignes vides sont ignorées. Les espaces autour du nom sont retirés.
    Une ligne mal formée (pas de point-virgule, ou note non numérique) est
    ignorée elle aussi : un fichier abîmé ne doit pas faire tomber le
    programme entier.
    Fichier absent -> dictionnaire vide.
    """
    pass


def ajouter_note(chemin, nom, note):
    """Ajoute une ligne « nom;note » à la fin du fichier, sans rien écraser.

    Si la note n'est pas comprise entre 0 et 20, lève une ValueError et
    n'écrit rien du tout.
    Ne renvoie rien.
    """
    pass


def diviser(a, b):
    """Renvoie a / b, ou None si b vaut zéro.

    C'est un entraînement à try / except sur un cas simple :
    attrape ZeroDivisionError, ne teste pas b == 0 à la main.
    """
    pass


if __name__ == "__main__":
    from pathlib import Path

    essai = Path(__file__).parent / "essai.txt"
    ecrire_lignes(essai, ["Alice;15", "Bob;12"])
    print(lire_lignes(essai))
    print(charger_notes(essai))
    ajouter_note(essai, "Chloé", 18)
    print(charger_notes(essai))
    print(diviser(10, 0))
    essai.unlink()
