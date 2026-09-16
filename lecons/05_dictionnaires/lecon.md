# Leçon 5 — Les dictionnaires

## Ce que tu sauras faire à la fin

Associer des informations entre elles, compter, regrouper — et arrêter d'empiler
des listes parallèles.

## Le problème que ça résout

Sans dictionnaire, pour stocker les notes de trois élèves :

```python
noms = ["Alice", "Bob", "Chloé"]
notes = [15, 12, 18]
```

Ça marche… tant que les deux listes restent alignées. Le jour où tu en tries une
seule, tout est faux, et silencieusement. Avec un dictionnaire :

```python
notes = {"Alice": 15, "Bob": 12, "Chloé": 18}
```

L'association est portée par la structure elle-même. On ne peut plus la casser.

## Lire, écrire

```python
notes["Alice"]          # 15
notes["Bob"] = 14       # modifie
notes["David"] = 11     # ajoute — même syntaxe
"Alice" in notes        # True
len(notes)              # 4
del notes["David"]      # supprime
```

Demander une clé absente provoque une `KeyError`. Pour l'éviter :

```python
notes.get("Inconnu")        # None, sans erreur
notes.get("Inconnu", 0)     # 0, la valeur de repli qu'on choisit
```

`.get()` avec une valeur de repli est l'outil central de cette leçon. Il
transforme « je dois d'abord vérifier si la clé existe » en une seule expression.

## Parcourir

```python
for nom in notes:                     # les clés
    print(nom)

for nom, note in notes.items():       # les deux à la fois — le plus utile
    print(f"{nom} : {note}")

notes.keys()      # les clés
notes.values()    # les valeurs
```

## Le motif du comptage

Celui-là, tu le réécriras cent fois :

```python
comptes = {}
for mot in mots:
    comptes[mot] = comptes.get(mot, 0) + 1
```

Ligne à déplier : « la nouvelle valeur pour `mot`, c'est son compte actuel — ou
zéro s'il n'y en a pas encore — plus un ». Sans `.get`, il faudrait un `if` pour
distinguer la première rencontre des suivantes.

Le motif jumeau, pour regrouper :

```python
groupes = {}
for mot in mots:
    initiale = mot[0]
    groupes[initiale] = groupes.get(initiale, []) + [mot]
```

## Ce qui peut servir de clé

Du texte, des nombres, des tuples — toute valeur non modifiable. Une liste ne
peut pas être une clé. Les clés sont uniques : réaffecter une clé existante
remplace sa valeur, elle ne s'ajoute pas.

Depuis Python 3.7, un dictionnaire conserve l'ordre d'insertion des clés.

## Découper du texte

Pour les exercices :

```python
"bonjour le monde".split()        # ["bonjour", "le", "monde"]
"a,b,c".split(",")                # ["a", "b", "c"]
"Bonjour".lower()                 # "bonjour"
"  du texte  ".strip()            # "du texte" (retire les espaces aux bords)
```

## À faire maintenant

1. `python3 exemple.py`
2. Complète `exercice.py`
3. `python3 ../../verifier.py 05`

## À me demander

- « Déroule-moi `comptes[mot] = comptes.get(mot, 0) + 1` sur trois mots. »
- « Quand utiliser un dictionnaire plutôt qu'une liste ? Donne-moi trois cas
  de chaque. »
