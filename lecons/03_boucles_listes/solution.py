"""Leçon 3 — solution. À n'ouvrir qu'après avoir cherché."""


def somme(nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total


def maximum(nombres):
    if len(nombres) == 0:
        raise ValueError("Liste vide")
    # On part du premier élément, jamais de 0 : sinon une liste de nombres
    # négatifs renverrait 0, qui n'en fait pas partie.
    plus_grand = nombres[0]
    for nombre in nombres:
        if nombre > plus_grand:
            plus_grand = nombre
    return plus_grand


def moyenne(nombres):
    if len(nombres) == 0:
        return 0.0
    return round(somme(nombres) / len(nombres), 2)


def pairs(nombres):
    resultat = []
    for nombre in nombres:
        if nombre % 2 == 0:
            resultat.append(nombre)
    return resultat


def compter(nombres, seuil):
    combien = 0
    for nombre in nombres:
        if nombre > seuil:
            combien += 1
    return combien


def inverser(elements):
    resultat = []
    for indice in range(len(elements) - 1, -1, -1):
        resultat.append(elements[indice])
    return resultat
