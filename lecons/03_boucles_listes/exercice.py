"""Leçon 3 — à toi de jouer. Vérifie avec : python3 ../../verifier.py 03"""


def somme(nombres):
    """Renvoie la somme des éléments de la liste, SANS utiliser sum().

    somme([1, 2, 3]) -> 6
    somme([])        -> 0

    Sers-toi du motif de l'accumulateur.
    """
    pass


def maximum(nombres):
    """Renvoie le plus grand élément, SANS utiliser max().

    maximum([12, 15, 8]) -> 15
    maximum([-5, -2])    -> -2

    Si la liste est vide, lève une ValueError("Liste vide").
    Piège : ne pars pas de 0 comme valeur de départ — regarde le deuxième
    exemple pour comprendre pourquoi.
    """
    pass


def moyenne(nombres):
    """Renvoie la moyenne, arrondie à 2 décimales.

    moyenne([10, 20]) -> 15.0
    moyenne([12, 15, 8, 19]) -> 13.5

    Si la liste est vide, renvoie 0.0 (pas d'erreur ici : une moyenne de rien
    vaut conventionnellement zéro dans cet exercice).
    """
    pass


def pairs(nombres):
    """Renvoie une NOUVELLE liste contenant seulement les nombres pairs.

    pairs([1, 2, 3, 4]) -> [2, 4]
    L'ordre d'origine doit être conservé.
    La liste reçue ne doit pas être modifiée.
    """
    pass


def compter(nombres, seuil):
    """Renvoie combien d'éléments sont strictement supérieurs au seuil.

    compter([1, 5, 9], 4) -> 2
    """
    pass


def inverser(elements):
    """Renvoie une nouvelle liste avec les éléments en ordre inverse.

    inverser([1, 2, 3]) -> [3, 2, 1]

    Fais-le avec une boucle, sans .reverse() ni [::-1] : l'intérêt est de
    manipuler les indices une fois consciemment.
    Indice : range(len(elements) - 1, -1, -1) parcourt les indices à l'envers.
    """
    pass


if __name__ == "__main__":
    notes = [12, 15, 8, 19]
    print(somme(notes))
    print(maximum(notes))
    print(moyenne(notes))
    print(pairs(notes))
    print(compter(notes, 10))
    print(inverser(notes))
