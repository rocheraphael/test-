"""Leçon 2 — à retaper et à lancer : python3 exemple.py"""

note = 15

# Les conditions sont testées dans l'ordre ; la première vraie l'emporte.
if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 10:
    mention = "Passable"
else:
    mention = "Insuffisant"

print(f"Note {note} -> {mention}")

# Combiner des conditions.
age = 20
a_le_permis = True

if age >= 18 and a_le_permis:
    print("Peut conduire.")
else:
    print("Ne peut pas conduire.")

# Un booléen se teste directement, sans « == True ».
pluie = False
if not pluie:
    print("On sort.")

# L'encadrement, qui se lit comme en mathématiques.
temperature = 22
if 18 <= temperature <= 25:
    print("Température agréable.")

# Refuser une valeur absurde plutôt que de calculer n'importe quoi.
saisie = 25
if not 0 <= saisie <= 20:
    print("Cette note est impossible : on lèverait une erreur ici.")
