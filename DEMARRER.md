# Installer et lancer les commandes

Tu n'as jamais ouvert de terminal ? C'est le bon moment. Compte vingt minutes
pour cette page, une seule fois.

> **Sur téléphone Android ?** Va directement à `ANDROID.md`. Tout ce parcours
> fonctionne depuis un téléphone, mais les étapes sont différentes.

Il y a trois choses à mettre en place, dans cet ordre :

1. **Python** sur ton ordinateur
2. **Le code** de ce dépôt, récupéré depuis GitHub
3. **Un terminal** ouvert au bon endroit

---

## 1. Installer Python

### Windows

Va sur <https://www.python.org/downloads/> et clique sur le gros bouton
« Download Python ».

Lance le fichier téléchargé. **Sur le premier écran, coche la case
« Add python.exe to PATH »** avant de cliquer sur Install. Elle est en bas, elle
est petite, et l'oublier est la cause d'à peu près tous les problèmes de
débutant sous Windows : sans elle, le terminal ne saura pas où trouver Python.

### macOS

Même adresse : <https://www.python.org/downloads/>, bouton « Download Python »,
puis tu ouvres le `.pkg` et tu suis les étapes.

macOS contient déjà une version de Python, mais elle appartient au système et
vaut mieux ne pas y toucher. Installe celle de python.org.

### Linux

Python 3 est déjà là dans presque toutes les distributions. Si ce n'est pas le
cas, sur Debian ou Ubuntu :

```
sudo apt install python3 git
```

---

## 2. Récupérer le code

Le code se trouve ici, sur la branche `claude/python-ai-assisted-learning-vbxaz3` :

<https://github.com/rocheraphael/test-/tree/claude/python-ai-assisted-learning-vbxaz3>

Deux façons de le rapatrier. **La première suffit largement pour commencer.**

### Façon simple : télécharger un dossier

1. Ouvre ce lien direct :
   <https://github.com/rocheraphael/test-/archive/refs/heads/claude/python-ai-assisted-learning-vbxaz3.zip>

   > Ce dépôt est **privé** : le lien ne fonctionne que dans un navigateur où tu
   > es déjà connecté à ton compte GitHub. Si tu obtiens une page « 404 », c'est
   > qu'il faut te connecter d'abord.
2. Décompresse le fichier `.zip` obtenu (double-clic sur Mac, clic droit →
   « Extraire tout » sur Windows).
3. Déplace le dossier obtenu là où tu veux — par exemple dans `Documents`.
   Renomme-le `python` si son nom est trop long, ça n'a aucune importance.

Inconvénient : si je modifie le dépôt plus tard, tu devras retélécharger.

### Façon durable : git

`git` est l'outil qui gère les versions du code. Tu l'apprendras un jour, mais
tu peux t'en servir dès maintenant avec deux commandes.

Sous Windows, installe-le d'abord : <https://git-scm.com/download/win>
(accepte toutes les options par défaut). Sur Mac, taper `git` dans le Terminal
proposera de l'installer.

Ensuite, dans un terminal :

```
git clone -b claude/python-ai-assisted-learning-vbxaz3 https://github.com/rocheraphael/test-.git
```

> Le dépôt étant privé, `git` va demander une authentification. GitHub n'accepte
> plus le mot de passe du compte : il faut un *personal access token*, ou rendre
> le dépôt public. Voir la section « Récupérer le code » de `ANDROID.md`, qui
> détaille les deux, et vaut aussi pour un ordinateur.

Un dossier `test-` apparaît là où tu étais. Pour récupérer mes modifications
plus tard, il suffira d'un `git pull` depuis ce dossier.

---

## 3. Ouvrir un terminal au bon endroit

Le terminal est une fenêtre où tu tapes des commandes au lieu de cliquer. Le
point important, celui qui bloque tout le monde au début : **le terminal est
toujours « situé » dans un dossier**. Quand tu tapes `python3 verifier.py`, il
cherche ce fichier dans le dossier où il se trouve. Si tu n'y es pas, il te dira
qu'il ne le trouve pas.

### La méthode que je te recommande : VS Code

C'est un éditeur de code gratuit, qui contient un terminal intégré déjà placé au
bon endroit. Ça t'évite toute la gymnastique de navigation.

1. Installe-le : <https://code.visualstudio.com/>
2. Ouvre-le, puis menu **Fichier → Ouvrir le dossier…** et choisis le dossier
   que tu viens de récupérer.
3. Menu **Terminal → Nouveau terminal**. Une zone s'ouvre en bas de la fenêtre.
   Tu es déjà dans le bon dossier.

Tu as maintenant les fichiers à gauche, ton code au milieu, le terminal en bas.
C'est l'installation de travail classique.

### Sans VS Code

**Windows** — Ouvre le dossier dans l'Explorateur de fichiers. Clique dans la
barre d'adresse en haut, efface ce qu'elle contient, tape `powershell` et
appuie sur Entrée. Un terminal s'ouvre, déjà dans ce dossier.

**macOS** — Ouvre l'application Terminal (⌘ + Espace, puis tape « Terminal »).
Tape `cd ` (avec l'espace après), puis **fais glisser le dossier depuis le
Finder dans la fenêtre du Terminal** : le chemin s'écrit tout seul. Appuie sur
Entrée.

**Linux** — Clic droit dans le dossier → « Ouvrir un terminal ici », ou
`Ctrl + Alt + T` puis `cd chemin/vers/le/dossier`.

---

## 4. Lancer les commandes

Vérifie d'abord que Python répond :

```
python3 --version
```

Tu dois voir quelque chose comme `Python 3.12.1`.

> **Sous Windows**, la commande s'appelle `python` et non `python3`. Partout
> dans ce dépôt, quand tu lis `python3`, tape `python`. Si `python` ouvre le
> Microsoft Store au lieu de répondre, c'est que la case « Add python.exe to
> PATH » n'a pas été cochée à l'installation : réinstalle en la cochant.

Puis, depuis le dossier du projet :

```
python3 verifier.py
```

Tu dois voir la liste des six leçons, toutes en rouge. C'est gagné : tout est
en place.

Les autres commandes du dépôt, par exemple :

```
python3 verifier.py 01
python3 lecons/01_variables/exemple.py
```

---

## Trois commandes de terminal à connaître

Elles suffisent pour tout ce parcours.

| Commande | Ce qu'elle fait |
|---|---|
| `pwd` (Windows : `cd` seul) | affiche dans quel dossier tu es |
| `ls` (Windows : `dir`) | liste les fichiers du dossier |
| `cd nom_du_dossier` | entre dans un dossier ; `cd ..` remonte d'un cran |

Deux gains de temps : la touche **Tab** complète un nom de fichier commencé, et
la **flèche du haut** rappelle la commande précédente. Sers-t'en dès le premier
jour, ce sont des dizaines d'heures économisées sur une vie de code.

---

## Quand ça ne marche pas

| Message | Ce qu'il signifie |
|---|---|
| `command not found: python3` <br> `'python' n'est pas reconnu…` | Python n'est pas installé, ou pas dans le PATH. Sous Windows : réinstalle en cochant la case. |
| `can't open file 'verifier.py': [Errno 2] No such file or directory` | Tu n'es pas dans le bon dossier. Tape `ls` (ou `dir`) : vois-tu `verifier.py` dans la liste ? Sinon, `cd` jusqu'au bon endroit. |
| `python3 : command not found` sur Windows | Utilise `python`, sans le 3. |
| Rien ne se passe, le curseur clignote | Un programme tourne encore. `Ctrl + C` l'interrompt. |

Si ça coince malgré tout : copie-moi **le message d'erreur en entier** et dis-moi
quel système tu utilises. Un message d'erreur complet vaut dix descriptions.
