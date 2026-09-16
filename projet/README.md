# Le projet : un carnet de notes en ligne de commande

Tu as fait six leçons. Chacune isolait un concept. Un vrai programme, c'est
l'inverse : tout arrive en même temps, et personne ne te dit quelles fonctions
écrire.

## Ce qu'on construit

Un programme qui se lance dans le terminal et permet de gérer les notes d'une
classe, enregistrées dans un fichier :

```
$ python3 carnet.py ajouter Alice 15
Note ajoutée : Alice, 15

$ python3 carnet.py ajouter Alice 17
Note ajoutée : Alice, 17

$ python3 carnet.py moyenne Alice
Alice : 16.00 de moyenne sur 2 notes

$ python3 carnet.py classement
1. Alice     16.00
2. Bob       12.50

$ python3 carnet.py moyenne Inconnu
Aucune note pour Inconnu.
```

## La méthode : une étape à la fois

Ne cherche pas à écrire le programme entier. Fais une étape, lance-la, vérifie
qu'elle marche, **puis** passe à la suivante. C'est la seule façon de savoir
quelle ligne a cassé quoi.

### Étape 1 — Le squelette

Un fichier `carnet.py` qui affiche juste ce qu'on lui a demandé.

```python
import sys

def main():
    arguments = sys.argv[1:]   # sys.argv[0] est le nom du script
    print(arguments)

if __name__ == "__main__":
    main()
```

Lance `python3 carnet.py ajouter Alice 15` et regarde ce qui s'affiche.
Remarque que `"15"` est du texte, pas un nombre — la leçon 1 revient te voir.

### Étape 2 — Le stockage

Écris deux fonctions, en te servant de la leçon 6 :

- `charger()` → renvoie `{nom: [notes]}` depuis `notes.txt`
- `sauvegarder(donnees)` → écrit ce dictionnaire dans `notes.txt`

Choisis toi-même le format de fichier. `Alice;15;17` est un choix raisonnable.
Teste ces deux fonctions **seules**, avant de brancher quoi que ce soit dessus.

### Étape 3 — La commande `ajouter`

Elle charge, ajoute la note à la bonne personne, sauvegarde. Refuse une note
hors de 0–20 avec un message clair — pas une trace d'erreur Python.

### Étape 4 — La commande `moyenne`

Leçon 5. Attention au cas où le nom n'existe pas, et au cas où la personne n'a
aucune note.

### Étape 5 — La commande `classement`

Trie les élèves par moyenne décroissante. Tu auras besoin de :

```python
sorted(moyennes.items(), key=lambda couple: couple[1], reverse=True)
```

Ne recopie pas cette ligne sans demander ce que `key=lambda` veut dire. C'est
exactement le moment où la règle du « je peux l'expliquer » s'applique.

### Étape 6 — Les cas tordus

Que se passe-t-il si on lance le programme sans argument ? Avec une commande
inconnue ? Avec `ajouter Alice` sans la note ? Chacun de ces cas doit produire
un message compréhensible.

## Ce que tu peux me demander à chaque étape

- « Voici mon plan pour l'étape 3, est-ce qu'il tient debout ? »
- « Mon `charger()` renvoie un dictionnaire vide alors que le fichier existe. »
- « Relis mon `carnet.py` et dis-moi ce qu'un développeur expérimenté
  changerait — sans le réécrire. »
- « Écris-moi des tests pour `charger()` et `sauvegarder()`. » — bonne demande :
  tu obtiens un filet de sécurité sans qu'on te prenne le code intéressant.

## Pour aller plus loin, une fois que ça marche

- Une commande `supprimer`.
- Des notes avec coefficients.
- Remplacer le format maison par du JSON (`import json`) — et comparer.
- Remplacer `sys.argv` par le module `argparse`, qui gère l'aide et les erreurs
  d'arguments pour toi.
