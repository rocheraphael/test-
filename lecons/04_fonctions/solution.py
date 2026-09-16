"""Leçon 4 — solution. À n'ouvrir qu'après avoir cherché."""


def repeter(texte, fois=2, separateur=" "):
    return separateur.join([texte] * fois)


def premier_superieur(nombres, seuil):
    for nombre in nombres:
        if nombre > seuil:
            return nombre
    return None


def appliquer(fonction, elements):
    resultat = []
    for element in elements:
        resultat.append(fonction(element))
    return resultat


def ajouter_course(article, liste=None):
    # Si la valeur par défaut était [], la MÊME liste servirait à tous les
    # appels et se remplirait au fil du programme.
    if liste is None:
        liste = []
    liste.append(article)
    return liste


def statistiques(nombres):
    if not nombres:
        return (None, None, 0.0)
    return (min(nombres), max(nombres), round(sum(nombres) / len(nombres), 2))
