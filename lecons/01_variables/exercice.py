"""Leçon 1 — à toi de jouer.

Remplace chaque `pass` par ton code. Vérifie avec :
    python3 ../../verifier.py 01
"""


def celsius_en_fahrenheit(celsius):
    """Convertit une température en degrés Fahrenheit.

    La formule est : fahrenheit = celsius * 9 / 5 + 32
    celsius_en_fahrenheit(100) doit renvoyer 212.0
    """
    pass


def prix_ttc(prix_ht, taux_tva):
    """Renvoie le prix TTC, arrondi à 2 décimales.

    Le taux est donné en pourcentage : taux_tva=20 signifie 20 %.
    prix_ttc(100, 20) doit renvoyer 120.0
    prix_ttc(19.99, 5.5) doit renvoyer 21.09

    Indice : la fonction round(nombre, 2) arrondit à deux décimales.
    """
    pass


def presentation(nom, age):
    """Renvoie une phrase de présentation.

    presentation("Alice", 30) doit renvoyer exactement :
        "Alice a 30 ans."

    Attention : on RENVOIE la phrase (return), on ne l'affiche pas (print).
    """
    pass


def est_pair(nombre):
    """Renvoie True si le nombre est pair, False sinon.

    est_pair(10) -> True
    est_pair(7)  -> False

    Indice : le reste de la division par 2 vaut 0 pour un nombre pair.
    Écris directement le test, sans if : une comparaison EST déjà un booléen.
    """
    pass


# Ce bloc ne s'exécute que si tu lances CE fichier directement.
# C'est ton bac à sable pour essayer des choses.
if __name__ == "__main__":
    print(celsius_en_fahrenheit(100))
    print(prix_ttc(100, 20))
    print(presentation("Alice", 30))
    print(est_pair(10))
