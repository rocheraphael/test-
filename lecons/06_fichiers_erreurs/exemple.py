"""Leçon 6 — à retaper et à lancer : python3 exemple.py

Ce script écrit un fichier à côté de lui, puis le relit.
"""

from pathlib import Path

DOSSIER = Path(__file__).parent
FICHIER = DOSSIER / "notes_exemple.txt"

# Écrire. "w" écrase le contenu précédent ; le \n ne s'ajoute pas tout seul.
with open(FICHIER, "w", encoding="utf-8") as fichier:
    fichier.write("Alice;15\n")
    fichier.write("Bob;12\n")
    fichier.write("Chloé;18\n")

print(f"Fichier écrit : {FICHIER.name}")

# Relire ligne par ligne, et découper chaque ligne.
notes = {}
with open(FICHIER, encoding="utf-8") as fichier:
    for ligne in fichier:
        ligne = ligne.strip()          # sans ça, "18\n" au lieu de "18"
        if not ligne:                  # on saute les lignes vides
            continue
        nom, note = ligne.split(";")
        notes[nom] = int(note)

print(notes)

# Gérer l'absence du fichier plutôt que de planter.
try:
    with open(DOSSIER / "inexistant.txt", encoding="utf-8") as fichier:
        contenu = fichier.read()
except FileNotFoundError:
    contenu = ""
    print("Fichier absent : on repart d'un contenu vide.")

# Gérer une conversion impossible.
for saisie in ["12", "douze"]:
    try:
        print(f"{saisie!r} -> {int(saisie)}")
    except ValueError:
        print(f"{saisie!r} n'est pas un nombre entier.")

# Ajouter à la fin avec "a", sans écraser.
with open(FICHIER, "a", encoding="utf-8") as fichier:
    fichier.write("David;11\n")

print(FICHIER.read_text(encoding="utf-8"))

# On nettoie derrière nous.
FICHIER.unlink()
