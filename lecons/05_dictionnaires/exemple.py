"""Leçon 5 — à retaper et à lancer : python3 exemple.py"""

notes = {"Alice": 15, "Bob": 12, "Chloé": 18}

# Lire, modifier, ajouter.
print(notes["Alice"])
notes["Bob"] = 14
notes["David"] = 11
print(notes)

# Une clé absente lève une KeyError ; .get() évite le plantage.
print(notes.get("Inconnu"))        # None
print(notes.get("Inconnu", 0))     # 0, la valeur de repli qu'on choisit

# Parcourir clés et valeurs ensemble : la forme la plus courante.
for nom, note in notes.items():
    print(f"{nom:<8} {note}")

# Le motif du comptage.
texte = "le chat dort le chien dort le chat mange"
comptes = {}
for mot in texte.split():
    comptes[mot] = comptes.get(mot, 0) + 1
print(comptes)

# Trouver la clé de plus grande valeur, avec le motif de l'accumulateur.
mot_frequent = None
meilleur = 0
for mot, nombre in comptes.items():
    if nombre > meilleur:
        meilleur = nombre
        mot_frequent = mot
print(f"Mot le plus fréquent : {mot_frequent} ({meilleur} fois)")

# Le motif du regroupement.
groupes = {}
for mot in texte.split():
    initiale = mot[0]
    groupes[initiale] = groupes.get(initiale, []) + [mot]
print(groupes)
