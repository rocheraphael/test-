"""Leçon 1 — à retaper et à lancer : python3 exemple.py"""

# Trois variables, trois types différents.
nom = "Alice"            # str  : du texte
age = 30                 # int  : un entier
taille = 1.68            # float: un nombre à virgule

print(nom, age, taille)
print(type(nom), type(age), type(taille))

# Le signe = se lit « reçoit ». Ici, age passe de 30 à 31.
age = age + 1
print(f"Après un anniversaire, {nom} a {age} ans.")

# Un calcul, puis un affichage arrondi à deux décimales.
imc = 62 / (taille ** 2)
print(f"IMC : {imc:.2f}")

# Le piège des types : ce qui vient d'un texte est un texte.
saisie = "25"                    # imagine que ça vienne de input()
print(saisie + saisie)           # "2525"  — collage de textes
print(int(saisie) + int(saisie)) # 50      — addition de nombres

# Le reste de la division : l'outil pour tester la parité.
print(f"10 est pair ? {10 % 2 == 0}")
print(f"7 est pair ? {7 % 2 == 0}")
