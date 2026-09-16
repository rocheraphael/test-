"""Leçon 1 — solution. À n'ouvrir qu'après avoir cherché."""


def celsius_en_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def prix_ttc(prix_ht, taux_tva):
    return round(prix_ht * (1 + taux_tva / 100), 2)


def presentation(nom, age):
    return f"{nom} a {age} ans."


def est_pair(nombre):
    # Une comparaison produit déjà True ou False : pas besoin de if.
    return nombre % 2 == 0
