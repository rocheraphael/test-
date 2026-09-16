"""Leçon 3 — à retaper et à lancer : python3 exemple.py"""

notes = [12, 15, 8, 19]

# Accéder par indice. Le premier est à 0.
print(notes[0], notes[-1], len(notes))

# Parcourir : la façon normale en Python.
for note in notes:
    print(f"Note : {note}")

# Le motif de l'accumulateur : une variable mise à jour à chaque tour.
total = 0
for note in notes:
    total += note
print(f"Total : {total}, moyenne : {total / len(notes):.2f}")

# Le même motif pour filtrer dans une nouvelle liste.
bonnes = []
for note in notes:
    if note >= 10:
        bonnes.append(note)
print(f"Notes au-dessus de la moyenne : {bonnes}")

# Le même motif pour chercher un maximum, sans utiliser max().
plus_grande = notes[0]
for note in notes:
    if note > plus_grande:
        plus_grande = note
print(f"Meilleure note : {plus_grande}")

# range répète un nombre connu de fois. La borne de fin est exclue.
for i in range(1, 6):
    print(f"{i} au carré = {i ** 2}")

# while : tant que la condition tient.
reste = 100
tours = 0
while reste > 0:
    reste -= 30
    tours += 1
print(f"{tours} retraits de 30 pour épuiser 100 (reste : {reste})")
