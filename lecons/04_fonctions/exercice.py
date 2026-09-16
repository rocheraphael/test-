"""Leçon 4 — à toi de jouer. Vérifie avec : python3 ../../verifier.py 04"""


def repeter(texte, fois=2, separateur=" "):
    """Renvoie le texte répété, les copies séparées par le séparateur.

    repeter("ha")                      -> "ha ha"
    repeter("ha", 3)                   -> "ha ha ha"
    repeter("ha", 3, "-")              -> "ha-ha-ha"
    repeter("ha", 1)                   -> "ha"

    Indice : separateur.join(liste_de_textes) colle une liste de chaînes.
    """
    pass


def premier_superieur(nombres, seuil):
    """Renvoie le premier nombre strictement supérieur au seuil.

    S'il n'y en a aucun, renvoie None.

    premier_superieur([1, 5, 9], 4) -> 5
    premier_superieur([1, 2], 10)   -> None

    Sers-toi du fait que return sort immédiatement de la fonction.
    """
    pass


def appliquer(fonction, elements):
    """Renvoie une nouvelle liste où la fonction a été appliquée à chaque élément.

    appliquer(len, ["a", "bb"])  -> [1, 2]

    Oui : en Python, une fonction peut être passée en argument comme une
    valeur ordinaire. C'est ce qui rend le langage souple.
    """
    pass


def ajouter_course(article, liste=None):
    """Ajoute un article à une liste de courses et renvoie la liste.

    Si aucune liste n'est fournie, en crée une nouvelle.

        ajouter_course("pain")               -> ["pain"]
        ajouter_course("lait", ["pain"])     -> ["pain", "lait"]

    Deux appels sans liste doivent donner deux listes INDÉPENDANTES : c'est
    exactement le piège de la valeur par défaut mutable décrit dans la leçon.
    C'est pour cela que le paramètre vaut None et pas [].
    """
    pass


def statistiques(nombres):
    """Renvoie un tuple (minimum, maximum, moyenne arrondie à 2 décimales).

    statistiques([2, 4, 9]) -> (2, 9, 5.0)

    Sur une liste vide, renvoie (None, None, 0.0).
    Tu as le droit d'utiliser min(), max() et sum() à partir de maintenant.
    """
    pass


if __name__ == "__main__":
    print(repeter("ha", 3, "-"))
    print(premier_superieur([1, 5, 9], 4))
    print(appliquer(len, ["a", "bb"]))
    print(ajouter_course("pain"))
    print(statistiques([2, 4, 9]))
