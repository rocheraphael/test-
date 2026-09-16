# Apprendre Python pas à pas (avec une IA, sans se faire dépasser par elle)

Ce dépôt est un parcours d'apprentissage. Il ne contient pas un cours à lire
passivement : chaque leçon te demande d'écrire du code, et une commande te dit
si ce que tu as écrit fonctionne vraiment.

## Démarrage

Si tu n'as jamais ouvert de terminal, commence par **`DEMARRER.md`** : il
explique comment installer Python, récupérer ce dossier et lancer une commande.

Une fois que c'est fait, tout part d'ici :

```bash
python3 verifier.py
```

Cette commande passe en revue toutes les leçons et affiche où tu en es.
Au début, tout est rouge. C'est normal : tu n'as encore rien écrit.

Pour ne vérifier qu'une seule leçon :

```bash
python3 verifier.py 01
```

## Comment travailler une leçon

Chaque dossier `lecons/XX_.../` contient quatre fichiers, à ouvrir dans cet ordre :

| Fichier | Ce que tu en fais |
|---|---|
| `lecon.md` | Tu le **lis**. C'est l'explication du concept. |
| `exemple.py` | Tu le **retapes à la main** dans un fichier à toi, puis tu le lances. Ne fais pas de copier-coller : la mémoire passe par les doigts. |
| `exercice.py` | Tu le **complètes**. C'est là que tu travailles. |
| `test_exercice.py` | Tu n'y touches pas. C'est le juge. |
| `solution.py` | Tu ne l'ouvres **qu'après** avoir fait l'exercice, même raté. |

Lancer un fichier :

```bash
python3 lecons/01_variables/exemple.py
```

## Le parcours

1. `01_variables` — variables, types, opérations, affichage
2. `02_conditions` — `if` / `elif` / `else`, booléens, comparaisons
3. `03_boucles_listes` — listes, `for`, `while`, parcours et accumulation
4. `04_fonctions` — définir, appeler, retourner ; arguments et portée
5. `05_dictionnaires` — associer des clés à des valeurs, compter, regrouper
6. `06_fichiers_erreurs` — lire et écrire des fichiers, gérer les erreurs
7. `projet/` — un vrai petit programme, construit étape par étape

## Et l'IA dans tout ça ?

Lis `METHODE.md`. C'est la partie la plus importante du dépôt : elle explique
comment te servir de moi pour **apprendre** plutôt que pour **éviter d'apprendre**.
