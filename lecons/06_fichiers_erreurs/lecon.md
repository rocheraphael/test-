# Leçon 6 — Fichiers et erreurs

## Ce que tu sauras faire à la fin

Faire persister des données au-delà de la fin du programme, et réagir proprement
quand le monde extérieur ne coopère pas.

C'est la leçon qui fait passer de l'exercice au programme utile : jusqu'ici, tout
ce que tu calculais disparaissait à la dernière ligne.

## Lire un fichier

```python
with open("notes.txt", encoding="utf-8") as fichier:
    contenu = fichier.read()
```

Trois choses :

- `with` ferme le fichier automatiquement, même si une erreur survient au
  milieu. Ouvre toujours tes fichiers comme ça.
- `encoding="utf-8"` : sans lui, Python utilise l'encodage par défaut du
  système, et tes accents finissent en charabia sur une autre machine. Mets-le
  systématiquement.
- `contenu` est **une seule chaîne**, sauts de ligne compris.

Pour travailler ligne par ligne, ce qui est presque toujours ce qu'on veut :

```python
with open("notes.txt", encoding="utf-8") as fichier:
    for ligne in fichier:
        ligne = ligne.strip()   # retire le saut de ligne final
        print(ligne)
```

Le `.strip()` n'est pas facultatif : sans lui, la dernière ligne de ton texte
contient un `\n` invisible qui fera échouer toutes tes comparaisons. C'est un
classique, et il coûte cher en temps de recherche.

## Écrire

```python
with open("sortie.txt", "w", encoding="utf-8") as fichier:
    fichier.write("première ligne\n")
    fichier.write("deuxième ligne\n")
```

Le `"w"` (*write*) **écrase** le fichier existant sans prévenir. `"a"` (*append*)
ajoute à la fin. Le `\n` n'est pas ajouté tout seul : à toi de le mettre.

## Les erreurs ne sont pas des échecs

Jusqu'ici, une erreur arrêtait ton programme. C'est le bon comportement pendant
que tu développes. Mais quand ton programme lit un fichier que l'utilisateur a
pu supprimer, planter n'est plus acceptable :

```python
try:
    with open("notes.txt", encoding="utf-8") as fichier:
        contenu = fichier.read()
except FileNotFoundError:
    contenu = ""
```

Le bloc `try` contient ce qui peut échouer ; `except` dit quoi faire pour un type
d'erreur précis.

**Attrape toujours une erreur nommée.** Écrire `except:` tout court, ou
`except Exception:`, attrape aussi les fautes de frappe dans ton propre code et
les fait disparaître silencieusement. Tu passeras des heures à chercher un bug
que tu as toi-même masqué.

Les erreurs que tu croiseras le plus :

| Erreur | Cause typique |
|---|---|
| `FileNotFoundError` | le chemin n'existe pas |
| `ValueError` | `int("douze")` |
| `KeyError` | une clé absente d'un dictionnaire |
| `IndexError` | un indice hors de la liste |
| `TypeError` | `"3" + 4` |
| `ZeroDivisionError` | une moyenne sur une liste vide |

## Les autres blocs

```python
try:
    valeur = int(saisie)
except ValueError:
    print("Ce n'est pas un nombre.")
else:
    print("Conversion réussie.")   # seulement si aucune erreur
finally:
    print("On passe ici dans tous les cas.")
```

## Lever plutôt que masquer

Rattraper une erreur n'a de sens que si tu sais quoi faire à la place. Sinon,
laisse-la remonter, ou remplace-la par un message plus clair :

```python
if not chemin.endswith(".txt"):
    raise ValueError(f"Fichier non pris en charge : {chemin}")
```

Une bonne règle : rattrape près de l'utilisateur, lève près du calcul.

## Les chemins

```python
from pathlib import Path

dossier = Path("donnees")
fichier = dossier / "notes.txt"    # la barre oblique construit le chemin
fichier.exists()
fichier.read_text(encoding="utf-8")
```

`pathlib` est plus sûr que de coller des chaînes à la main, et fonctionne
identiquement sur Windows, macOS et Linux.

## À faire maintenant

1. `python3 exemple.py` — il crée et relit un fichier dans son dossier.
2. Complète `exercice.py`
3. `python3 ../../verifier.py 06`

## À me demander

- « Que se passe-t-il si j'ouvre en "w" un fichier qui contient déjà des
  données ? » (Réponse courte : elles sont perdues. Vérifie par toi-même.)
- « Montre-moi un bug rendu invisible par un `except:` trop large. »
