"""Leçon 5 — solution. À n'ouvrir qu'après avoir cherché."""


def compter_mots(texte):
    comptes = {}
    for mot in texte.lower().split():
        comptes[mot] = comptes.get(mot, 0) + 1
    return comptes


def mot_le_plus_frequent(texte):
    comptes = compter_mots(texte)
    meilleur_mot = None
    meilleur_compte = 0
    for mot, compte in comptes.items():
        # Strictement supérieur : en cas d'égalité, le premier vu reste.
        if compte > meilleur_compte:
            meilleur_mot = mot
            meilleur_compte = compte
    return meilleur_mot


def inverser_dictionnaire(dico):
    inverse = {}
    for cle, valeur in dico.items():
        inverse[valeur] = cle
    return inverse


def fusionner_stocks(stock_a, stock_b):
    # dict(stock_a) fabrique une copie : on ne touche pas à l'original.
    fusion = dict(stock_a)
    for article, quantite in stock_b.items():
        fusion[article] = fusion.get(article, 0) + quantite
    return fusion


def regrouper_par_initiale(mots):
    groupes = {}
    for mot in mots:
        initiale = mot[0].lower()
        groupes[initiale] = groupes.get(initiale, []) + [mot]
    return groupes


def moyenne_par_eleve(notes):
    moyennes = {}
    for eleve, ses_notes in notes.items():
        if ses_notes:
            moyennes[eleve] = round(sum(ses_notes) / len(ses_notes), 2)
        else:
            moyennes[eleve] = 0.0
    return moyennes
