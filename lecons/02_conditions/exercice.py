"""Leçon 2 — à toi de jouer. Vérifie avec : python3 ../../verifier.py 02"""


def mention(note):
    """Renvoie la mention correspondant à une note sur 20.

        note >= 16          -> "Très bien"
        16 > note >= 14     -> "Bien"
        14 > note >= 10     -> "Passable"
        note < 10           -> "Insuffisant"

    Si la note n'est pas entre 0 et 20 inclus, lève une ValueError :
        raise ValueError("Note invalide")

    Attention à l'ordre de tes conditions.
    """
    pass


def est_bissextile(annee):
    """Renvoie True si l'année est bissextile.

    La règle exacte : une année est bissextile si elle est divisible par 4,
    SAUF si elle est divisible par 100, MAIS quand même si elle est
    divisible par 400.

        2024 -> True   (divisible par 4)
        1900 -> False  (divisible par 100, mais pas par 400)
        2000 -> True   (divisible par 400)
        2023 -> False
    """
    pass


def tarif(age, jour):
    """Renvoie le prix d'un billet de cinéma, en euros (int).

        moins de 14 ans          -> 6
        14 ans ou plus, mais le jour est "mercredi" -> 8
        sinon                    -> 11

    Le jour est une chaîne en minuscules.
    """
    pass


def signe(nombre):
    """Renvoie "positif", "négatif" ou "nul" selon le nombre.

    Attention à l'accent dans "négatif".
    """
    pass


if __name__ == "__main__":
    print(mention(15))
    print(est_bissextile(2024))
    print(tarif(30, "mercredi"))
    print(signe(-3))
