# Leçon 1 — Variables et types

## Ce que tu sauras faire à la fin

Stocker une valeur, la transformer, l'afficher, et savoir de quel *type* elle est.

## Une variable, c'est une étiquette

```python
age = 30
```

Python range la valeur `30` quelque part en mémoire et colle dessus l'étiquette
`age`. À partir de là, écrire `age` revient à écrire `30`.

Le signe `=` n'est pas l'égalité des mathématiques. Il se lit « reçoit ».
`age = age + 1` n'est pas une équation absurde : c'est « age reçoit sa valeur
actuelle plus un ».

Les noms de variables s'écrivent en minuscules, avec des tirets bas :
`prix_total`, `nombre_de_lignes`. Un bon nom dit ce que la valeur *est*, pas
comment elle est calculée.

## Les quatre types que tu croiseras tout le temps

| Type | Exemple | À quoi ça sert |
|---|---|---|
| `int` | `42` | des nombres entiers |
| `float` | `3.14` | des nombres à virgule (avec un **point**, pas une virgule) |
| `str` | `"bonjour"` | du texte, entre guillemets |
| `bool` | `True` / `False` | vrai ou faux (majuscule obligatoire) |

Pour connaître le type d'une valeur : `type(age)`.

## Le piège numéro un du débutant

`"3"` et `3` ne sont pas la même chose.

```python
"3" + "4"    # donne "34"  — Python colle deux textes
 3  +  4     # donne 7     — Python additionne deux nombres
```

Et `"3" + 4` provoque une erreur : Python refuse de deviner ce que tu voulais.
C'est une bonne chose — c'est une erreur immédiate plutôt qu'un résultat faux
découvert trois semaines plus tard.

Pour passer de l'un à l'autre : `int("3")` et `str(3)`.

Cela compte dès que tu lis ce que tape un utilisateur : `input()` renvoie
**toujours** du texte, même si la personne tape `25`.

## Les opérations

```python
7 + 2   # 9
7 - 2   # 5
7 * 2   # 14
7 / 2   # 3.5   -> division, donne toujours un float
7 // 2  # 3     -> division entière, on jette la partie décimale
7 % 2   # 1     -> le reste. Très utile : n % 2 == 0 teste si n est pair
7 ** 2  # 49    -> puissance
```

## Afficher, proprement

La façon moderne, appelée *f-string* (le `f` avant le guillemet est
indispensable) :

```python
nom = "Alice"
age = 30
print(f"{nom} a {age} ans.")
```

Tout ce qui est entre accolades est évalué comme du code Python. On peut y
mettre un calcul : `f"L'an prochain : {age + 1}"`.

Pour arrondir un nombre à l'affichage : `f"{3.14159:.2f}"` donne `3.14`.

## À faire maintenant

1. Retape `exemple.py` dans un fichier à toi, puis lance-le :
   `python3 exemple.py`
2. Modifie une valeur, relance, observe.
3. Ouvre `exercice.py` et complète les trois fonctions.
4. Vérifie : `python3 ../../verifier.py 01`

## Si tu veux creuser, demande-moi

- « Pourquoi `0.1 + 0.2` ne donne pas exactement `0.3` ? »
- « Montre-moi trois erreurs classiques de conversion de type et leur message. »
- « Interroge-moi sur la différence entre `/` et `//`. »
