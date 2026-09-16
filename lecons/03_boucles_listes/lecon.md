# Leçon 3 — Listes et boucles

## Ce que tu sauras faire à la fin

Ranger plusieurs valeurs ensemble, les parcourir une par une, et en tirer un
résultat.

## Une liste

```python
notes = [12, 15, 8, 19]
```

Une liste garde ses éléments **dans l'ordre**, et on y accède par leur position,
appelée *indice*. Le premier élément est à l'indice **0**, pas 1.

```python
notes[0]    # 12  — le premier
notes[3]    # 19  — le quatrième
notes[-1]   # 19  — le dernier, sans avoir à compter
len(notes)  # 4   — combien d'éléments
```

Demander `notes[4]` provoque une `IndexError` : il n'y a rien à cette position.
Tu verras beaucoup cette erreur, elle vient presque toujours d'un décalage de 1.

Modifier une liste :

```python
notes.append(17)     # ajoute à la fin
notes[0] = 13        # remplace le premier
```

## La boucle `for`

C'est la construction que tu écriras le plus souvent en Python :

```python
for note in notes:
    print(note)
```

Ça se lit : « pour chaque note dans notes ». À chaque tour, la variable `note`
prend la valeur suivante. Tu n'as pas à gérer d'indice, et donc pas d'occasion
de te tromper d'un cran.

Si tu as vraiment besoin de la position :

```python
for indice, note in enumerate(notes):
    print(f"Note n°{indice + 1} : {note}")
```

## Le motif de l'accumulateur

Il revient sans arrêt. Le principe : une variable qui garde le résultat partiel,
et qu'on met à jour à chaque tour.

```python
total = 0                 # on part de zéro
for note in notes:
    total = total + note  # on ajoute chaque élément
print(total)
```

`total += note` est une écriture abrégée de `total = total + note`.

Le même motif sert à compter, à chercher un maximum, à construire une nouvelle
liste :

```python
bonnes = []
for note in notes:
    if note >= 10:
        bonnes.append(note)
```

Une fois ce motif compris, tu peux écrire à peu près n'importe quel traitement
de liste. Prends le temps qu'il faut ici.

## `range`, pour répéter

```python
for i in range(5):        # 0, 1, 2, 3, 4  — cinq tours
    print(i)

for i in range(1, 11):    # de 1 à 10 inclus
    print(i)
```

La borne de fin est toujours **exclue**. `range(5)` s'arrête à 4.

## La boucle `while`

Elle tourne tant qu'une condition reste vraie :

```python
reste = 100
while reste > 0:
    reste -= 30
```

Utilise-la quand tu ne sais pas d'avance combien de tours il faudra. Le danger :
si la condition ne devient jamais fausse, le programme tourne indéfiniment.
`Ctrl+C` interrompt.

En cas de doute, préfère `for` : la plupart des `while` de débutant sont des
`for` déguisés.

## Les raccourcis, à connaître mais pas tout de suite

Python fournit `sum(notes)`, `max(notes)`, `min(notes)`, `sorted(notes)`. Tu les
utiliseras tous les jours.

Mais dans l'exercice qui suit, on te demande parfois de les réécrire à la main.
Ce n'est pas pour t'embêter : savoir reconstruire `max` est ce qui te permettra,
plus tard, d'écrire les traitements pour lesquels aucune fonction toute faite
n'existe.

## À faire maintenant

1. `python3 exemple.py`
2. Complète `exercice.py`
3. `python3 ../../verifier.py 03`

## À me demander

- « Fais-moi dérouler cette boucle tour par tour, avec la valeur des variables. »
  (C'est la meilleure question de cette leçon.)
- « Pourquoi ma liste est vide à la fin ? »
