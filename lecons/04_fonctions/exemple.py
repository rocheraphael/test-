"""Leçon 4 — à retaper et à lancer : python3 exemple.py"""


def prix_ttc(prix_ht, taux=20):
    """Prix TTC. Le taux vaut 20 % si on ne le précise pas."""
    return round(prix_ht * (1 + taux / 100), 2)


print(prix_ttc(100))          # utilise la valeur par défaut
print(prix_ttc(100, 5.5))     # on impose le taux
print(prix_ttc(taux=10, prix_ht=100))  # on peut nommer les arguments


# return contre print : la différence qui compte.
def double_affiche(n):
    print(n * 2)


def double_renvoie(n):
    return n * 2


double_affiche(5)                    # affiche 10, renvoie None
resultat = double_renvoie(5)         # n'affiche rien, renvoie 10
print(f"Et on peut réutiliser : {resultat + 1}")


# return sort immédiatement de la fonction.
def premier_negatif(nombres):
    """Renvoie le premier nombre négatif, ou None s'il n'y en a pas."""
    for nombre in nombres:
        if nombre < 0:
            return nombre     # on sort dès qu'on l'a trouvé
    return None               # atteint seulement si la boucle s'est épuisée


print(premier_negatif([3, 7, -2, -9]))
print(premier_negatif([3, 7]))


# Des petites fonctions qui se combinent.
def somme(nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total


def moyenne(nombres):
    return somme(nombres) / len(nombres)


print(moyenne([12, 15, 8, 19]))


# La portée : ce qui est né dans une fonction reste dans la fonction.
def essai():
    interne = "je n'existe qu'ici"
    return interne


print(essai())
# print(interne)  # décommente cette ligne pour voir la NameError
