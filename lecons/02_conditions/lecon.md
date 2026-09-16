# Leçon 2 — Les conditions

## Ce que tu sauras faire à la fin

Faire prendre des décisions à ton programme selon les valeurs qu'il manipule.

## La forme de base

```python
if temperature > 30:
    print("Il fait chaud.")
```

Deux choses à retenir, et elles causent 90 % des erreurs de débutant :

- Les **deux points** à la fin de la ligne `if`.
- L'**indentation** : les lignes qui dépendent du `if` sont décalées de quatre
  espaces. En Python, ce décalage n'est pas cosmétique, c'est la syntaxe. C'est
  lui qui dit où le bloc commence et où il finit.

## Les trois branches

```python
if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
else:
    mention = "Passable"
```

`elif` = « sinon si ». Python teste les conditions **dans l'ordre** et
s'arrête à la première qui est vraie. C'est pour cela qu'on écrit `>= 16` avant
`>= 14` : une note de 18 satisfait les deux, et c'est la première rencontrée
qui gagne.

Inverser cet ordre est une erreur classique, et le programme ne plantera pas —
il donnera simplement des résultats faux. Les tests sont là pour ça.

## Comparer

```python
a == b   # égal      (deux signes ! un seul, c'est l'affectation)
a != b   # différent
a <  b   a <= b   a >  b   a >= b
```

Une comparaison produit un booléen. Donc ceci :

```python
if est_majeur == True:
```

s'écrit simplement :

```python
if est_majeur:
```

## Combiner

```python
if age >= 18 and permis_valide:
    ...
if jour == "samedi" or jour == "dimanche":
    ...
if not connecte:
    ...
```

Python autorise aussi une écriture que peu de langages permettent :

```python
if 0 <= note <= 20:
```

qui se lit exactement comme en mathématiques.

## Lever une erreur volontairement

Quand on te donne une valeur absurde, mieux vaut refuser bruyamment que
renvoyer n'importe quoi :

```python
if note < 0 or note > 20:
    raise ValueError("La note doit être comprise entre 0 et 20.")
```

`raise` interrompt la fonction immédiatement. Tu verras en leçon 6 comment
rattraper ces erreurs.

## À faire maintenant

1. Lance `python3 exemple.py`, puis modifie les valeurs et relance.
2. Complète `exercice.py`.
3. Vérifie : `python3 ../../verifier.py 02`

## À me demander si ça résiste

- « Montre-moi ce qui se passe si j'oublie l'indentation, avec le message
  d'erreur exact. »
- « Donne-moi cinq conditions à traduire en Python, et corrige-moi. »
