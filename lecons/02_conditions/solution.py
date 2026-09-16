"""Leçon 2 — solution. À n'ouvrir qu'après avoir cherché."""


def mention(note):
    if not 0 <= note <= 20:
        raise ValueError("Note invalide")
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


def est_bissextile(annee):
    if annee % 400 == 0:
        return True
    if annee % 100 == 0:
        return False
    return annee % 4 == 0


def tarif(age, jour):
    if age < 14:
        return 6
    if jour == "mercredi":
        return 8
    return 11


def signe(nombre):
    if nombre > 0:
        return "positif"
    if nombre < 0:
        return "négatif"
    return "nul"
