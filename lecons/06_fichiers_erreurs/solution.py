"""Leçon 6 — solution. À n'ouvrir qu'après avoir cherché."""


def lire_lignes(chemin):
    lignes = []
    try:
        with open(chemin, encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    lignes.append(ligne)
    except FileNotFoundError:
        return []
    return lignes


def ecrire_lignes(chemin, lignes):
    with open(chemin, "w", encoding="utf-8") as fichier:
        for ligne in lignes:
            fichier.write(f"{ligne}\n")


def charger_notes(chemin):
    notes = {}
    for ligne in lire_lignes(chemin):
        morceaux = ligne.split(";")
        if len(morceaux) != 2:
            continue                     # ligne mal formée : on l'ignore
        nom, valeur = morceaux
        try:
            notes[nom.strip()] = int(valeur.strip())
        except ValueError:
            continue                     # note non numérique : on l'ignore
    return notes


def ajouter_note(chemin, nom, note):
    # On valide AVANT d'ouvrir le fichier : ainsi rien n'est écrit en cas
    # d'erreur, et le fichier n'est pas laissé à moitié modifié.
    if not 0 <= note <= 20:
        raise ValueError(f"Note invalide : {note}")
    with open(chemin, "a", encoding="utf-8") as fichier:
        fichier.write(f"{nom};{note}\n")


def diviser(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
