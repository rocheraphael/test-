# Leçon 4 — Les fonctions

## Ce que tu sauras faire à la fin

Découper un programme en morceaux nommés, réutilisables, et testables séparément.

Tu écris des fonctions depuis la leçon 1 sans qu'on t'ait expliqué ce que c'est.
C'était volontaire : tu as maintenant l'intuition, on met les mots dessus.

## Anatomie

```python
def prix_ttc(prix_ht, taux):      # def, nom, paramètres, deux points
    montant = prix_ht * taux / 100  # le corps, indenté
    return prix_ht + montant        # ce que la fonction renvoie
```

- Les noms entre parenthèses (`prix_ht`, `taux`) sont les **paramètres** :
  des variables qui n'existent qu'à l'intérieur de la fonction.
- Quand tu écris `prix_ttc(100, 20)`, les valeurs `100` et `20` sont les
  **arguments**, et elles sont rangées dans les paramètres.

## `return` n'est pas `print`

C'est la confusion la plus tenace du débutant, alors prenons-la de front.

```python
def double_affiche(n):
    print(n * 2)

def double_renvoie(n):
    return n * 2
```

La première affiche un nombre à l'écran et renvoie `None` — rien.
La seconde n'affiche rien, mais **produit une valeur** que tu peux réutiliser :

```python
x = double_renvoie(5) + 1   # 11
y = double_affiche(5) + 1   # TypeError : on ne peut pas additionner None
```

Retiens ceci : `print` sert à parler à l'humain, `return` sert à parler au reste
du programme. Une fonction qui calcule doit `return`. L'affichage se fait à part.

`return` met aussi fin à la fonction immédiatement — les lignes en dessous ne
s'exécutent pas. C'est ce qui permet d'écrire :

```python
def maximum(a, b):
    if a > b:
        return a
    return b        # atteint seulement si on n'est pas déjà sorti
```

## Les valeurs par défaut

```python
def saluer(nom, salutation="Bonjour"):
    return f"{salutation}, {nom} !"

saluer("Alice")              # "Bonjour, Alice !"
saluer("Alice", "Salut")     # "Salut, Alice !"
```

Un paramètre avec valeur par défaut devient facultatif. Ils doivent tous être
placés après les paramètres obligatoires.

**Piège sérieux** : ne mets jamais une liste ou un dictionnaire comme valeur par
défaut (`def f(items=[])`). Cette liste est créée une seule fois et survit d'un
appel à l'autre — le bug est déroutant. On écrit `items=None` et on crée la
liste dans le corps. Demande-moi une démonstration, ça vaut le coup de la voir.

## La portée : ce qui vit où

```python
def compter():
    n = 0        # n naît ici
    return n     # et meurt à la sortie

compter()
print(n)         # NameError : n n'existe pas ici
```

Les variables d'une fonction lui sont propres. C'est une protection, pas une
limitation : tu peux appeler `n` une variable dans dix fonctions différentes sans
qu'elles se marchent dessus.

Corollaire : une fonction ne devrait dépendre que de ses paramètres. Une fonction
qui va lire une variable globale est difficile à tester et à déplacer.

## Une fonction bien faite

- Elle fait **une** chose, et son nom le dit (`calculer_moyenne`, pas `traiter`).
- Elle prend ses entrées en paramètres et renvoie son résultat.
- Elle n'affiche rien, sauf si son rôle est précisément d'afficher.
- Elle tient à l'écran. Au-delà de vingt lignes, il y en a deux qui se cachent
  dedans.

## La docstring

Le texte entre triples guillemets juste sous le `def` est une *docstring*. Elle
documente la fonction, et `help(ma_fonction)` l'affiche. Tous les exercices de ce
dépôt en ont — c'est une habitude à prendre tôt.

## À faire maintenant

1. `python3 exemple.py`
2. Complète `exercice.py`
3. `python3 ../../verifier.py 04`

## À me demander

- « Montre-moi le bug de la liste en valeur par défaut. »
- « Relis mes fonctions et dis-moi lesquelles font plus d'une chose. »
