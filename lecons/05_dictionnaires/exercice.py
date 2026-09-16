"""Leçon 5 — à toi de jouer. Vérifie avec : python3 ../../verifier.py 05"""


def compter_mots(texte):
    """Renvoie un dictionnaire {mot: nombre d'occurrences}.

    Les mots sont séparés par des espaces, et la casse est ignorée
    (« Le » et « le » comptent pour le même mot).

    compter_mots("le chat le")  -> {"le": 2, "chat": 1}
    compter_mots("")            -> {}

    Indice : texte.lower().split()
    """
    pass


def mot_le_plus_frequent(texte):
    """Renvoie le mot qui revient le plus souvent.

    En cas d'égalité, renvoie celui rencontré en premier.
    Sur un texte vide, renvoie None.

    mot_le_plus_frequent("le chat le chien le") -> "le"
    """
    pass


def inverser_dictionnaire(dico):
    """Échange les clés et les valeurs.

    inverser_dictionnaire({"a": 1, "b": 2}) -> {1: "a", 2: "b"}

    Si deux clés partagent la même valeur, la dernière rencontrée l'emporte.
    """
    pass


def fusionner_stocks(stock_a, stock_b):
    """Additionne deux inventaires {article: quantité}.

    fusionner_stocks({"pomme": 3}, {"pomme": 2, "poire": 1})
        -> {"pomme": 5, "poire": 1}

    Les deux dictionnaires reçus ne doivent pas être modifiés.
    """
    pass


def regrouper_par_initiale(mots):
    """Regroupe les mots selon leur première lettre (en minuscule).

    regrouper_par_initiale(["chat", "chien", "loup"])
        -> {"c": ["chat", "chien"], "l": ["loup"]}

    L'ordre d'apparition est conservé dans chaque groupe.
    """
    pass


def moyenne_par_eleve(notes):
    """Calcule la moyenne de chaque élève, arrondie à 2 décimales.

    moyenne_par_eleve({"Alice": [15, 17], "Bob": [10, 11, 12]})
        -> {"Alice": 16.0, "Bob": 11.0}

    Un élève sans aucune note a une moyenne de 0.0.
    """
    pass


if __name__ == "__main__":
    print(compter_mots("le chat le"))
    print(mot_le_plus_frequent("le chat le chien le"))
    print(fusionner_stocks({"pomme": 3}, {"pomme": 2, "poire": 1}))
    print(regrouper_par_initiale(["chat", "chien", "loup"]))
    print(moyenne_par_eleve({"Alice": [15, 17], "Bob": [10, 11, 12]}))
