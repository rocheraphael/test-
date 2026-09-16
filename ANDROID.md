# Coder ce parcours depuis un téléphone Android

Oui, c'est possible, et entièrement. Une précision d'abord, parce qu'elle
oriente tout le reste.

## La puissance n'est pas le sujet

Ton téléphone est sans commune mesure avec ce que demandent ces exercices. Un
Python qui calcule une moyenne sur quatre notes, c'est quelques microsecondes de
travail. Tu pourrais faire tourner ce parcours sur un téléphone de 2015.

Ce qui coince sur un téléphone, ce n'est pas le calcul, c'est la **saisie**.
Python est un langage où l'indentation fait partie de la syntaxe : quatre
espaces au début d'une ligne changent le sens du programme. Taper ça sur un
clavier tactile, avec la correction automatique qui s'en mêle, est franchement
pénible.

D'où la recommandation qui compte le plus dans cette page : **si tu comptes y
passer plus de quelques heures, achète un petit clavier Bluetooth.** Vingt à
trente euros. Il transforme complètement l'expérience, bien plus que n'importe
quel choix d'application.

Cela dit, on peut commencer sans, et voir.

## L'outil : Termux

Termux est un vrai terminal Linux sur Android. Python y tourne réellement — ce
n'est pas un simulateur. Les commandes du dépôt fonctionnent à l'identique.

### Où l'installer — attention à ce point

**N'installe pas Termux depuis le Play Store.** La version qui s'y trouve est
abandonnée depuis novembre 2020 et n'a reçu aucun correctif depuis ; ses dépôts
de paquets ne fonctionnent plus. Tu perdrais une soirée avant de comprendre
pourquoi rien ne s'installe.

Les deux sources officielles sont **F-Droid** et **GitHub** :

- F-Droid : <https://f-droid.org/en/packages/com.termux/>
  Tu peux télécharger l'APK directement depuis cette page, sans installer
  l'application F-Droid.
- GitHub : <https://github.com/termux/termux-app/releases>

Android te demandera d'autoriser l'installation depuis une source inconnue.
C'est normal pour une application hors Play Store.

### Quel fichier APK choisir sur GitHub

La page des releases propose plusieurs fichiers. Ils portent des noms de cette
forme :

```
termux-app_v0.118.3+github-debug_universal.apk
termux-app_v0.118.3+github-debug_arm64-v8a.apk
termux-app_v0.118.3+github-debug_armeabi-v7a.apk
termux-app_v0.118.3+github-debug_x86_64.apk
```

Ce qui change à la fin, c'est le **processeur** visé. Un téléphone ne sait
exécuter que le code compilé pour le sien.

**Prends celui qui finit par `universal`.** Il contient le code de toutes les
architectures : il fonctionne partout, sans que tu aies à savoir quel processeur
tu as. Il pèse environ deux fois plus lourd, ce qui est parfaitement indifférent
pour une application qu'on installe une fois.

Si tu préfères le fichier le plus léger : `arm64-v8a` est le bon choix pour
pratiquement tous les téléphones vendus depuis 2016. Les autres ne te concernent
pas — `armeabi-v7a` vise les vieux appareils 32 bits, `x86` et `x86_64` les
émulateurs et quelques tablettes Intel.

Deux détails qui inquiètent à tort :

- Le mot **`debug`** dans le nom est normal. Ce n'est pas une version bancale :
  c'est la façon dont Termux signe ses paquets distribués hors Play Store.
- Si tu vois des variantes **`apt-android-5`** et **`apt-android-7`** (sur des
  versions plus anciennes), prends `android-7` : elle vise Android 7 et
  au-delà, donc tout téléphone actuel.

### Un choix qui vous engage : F-Droid ou GitHub, pas les deux

Android refuse de mettre à jour une application avec un fichier signé par une
autre clé. Or les versions F-Droid et GitHub de Termux sont signées
différemment. Conséquence : pour passer de l'une à l'autre, il faut désinstaller
d'abord — **et la désinstallation efface tout ton dossier Termux**, code compris.

Décide donc maintenant et n'en change plus. Mon conseil pour toi : **F-Droid**,
parce que l'application F-Droid gère les mises à jour toute seule, alors qu'avec
GitHub tu devras revenir télécharger un APK à la main.

Dans les deux cas, pense à garder ton travail sur GitHub (ou ailleurs) plutôt
que seulement dans Termux. C'est vrai de tout code, sur toute machine.

### La première mise en route

Ouvre Termux et tape, une ligne à la fois (Entrée après chacune) :

```
pkg update
pkg upgrade
pkg install python git nano unzip
```

Réponds `y` si on te demande de confirmer. Compte quelques minutes.

Vérifie ensuite :

```
python --version
```

Dans Termux, `python` et `python3` marchent tous les deux.

### Survivre au clavier

Termux affiche une rangée de touches supplémentaires au-dessus du clavier :
`Ctrl`, `Alt`, `Tab`, les flèches. Si tu ne la vois pas, fais glisser vers le
haut depuis la zone du clavier, ou appuie sur **Volume haut + Q**.

Autre raccourci qui sert sans arrêt : **Volume bas + une lettre** donne
`Ctrl + cette lettre`. Par exemple Volume bas + C interrompt un programme qui
tourne.

## Récupérer le code

**Ton dépôt est privé.** C'est une information que je n'avais pas quand je t'ai
donné le lien de téléchargement direct plus tôt : il ne fonctionnera que dans un
navigateur où tu es connecté à GitHub, et un `git clone` te demandera un mot de
passe que GitHub n'accepte plus.

Trois chemins, du plus simple au plus propre.

### A. Par le navigateur (le plus simple)

1. Dans Chrome sur ton téléphone, connecte-toi à GitHub.
2. Ouvre ce lien — il télécharge un ZIP :
   <https://github.com/rocheraphael/test-/archive/refs/heads/claude/python-ai-assisted-learning-vbxaz3.zip>
3. Dans Termux :

```
termux-setup-storage
```

Android demande l'autorisation d'accéder aux fichiers : accepte. Puis :

```
ls ~/storage/downloads
```

Tu vois le nom exact du ZIP téléchargé. Décompresse-le (commence à taper le nom
et appuie sur **Tab** pour qu'il se complète tout seul) :

```
cd ~
unzip ~/storage/downloads/LE_NOM_DU_FICHIER.zip
ls
```

Un dossier apparaît. Entre dedans avec `cd` et son nom, puis :

```
python verifier.py
```

### B. Rendre le dépôt public

Si tu rends ce dépôt public — c'est un dépôt d'apprentissage, il ne contient
aucune donnée personnelle ni mot de passe — alors `git clone` fonctionne sans
aucune authentification :

```
git clone -b claude/python-ai-assisted-learning-vbxaz3 https://github.com/rocheraphael/test-.git
cd test-
python verifier.py
```

C'est le chemin le plus confortable sur la durée : un simple `git pull` te
rapporte ensuite mes modifications. En contrepartie, ton code d'apprentissage
devient visible par tout le monde. Beaucoup de gens apprennent en public sans
que ça pose problème ; c'est ton choix, pas le mien, et il se change dans les
deux sens à tout moment.

Dans l'application GitHub ou sur github.com : dépôt → Settings → tout en bas,
« Change repository visibility ».

### C. Avec un jeton d'accès

Si tu veux garder le dépôt privé **et** utiliser `git`, il faut un *personal
access token*. Sur github.com : ton avatar → Settings → Developer settings →
Personal access tokens → Fine-grained tokens → Generate new token. Donne-lui
accès à ce seul dépôt, en lecture.

GitHub n'affiche le jeton qu'une fois : copie-le immédiatement. Ensuite, le
`git clone` ci-dessus te demandera un nom d'utilisateur (le tien) et un mot de
passe (colle le jeton).

C'est la solution la plus propre, mais la plus pénible à faire sur un téléphone.
Ne commence pas par là.

## Écrire du code dans Termux

Pour modifier un fichier d'exercice :

```
nano lecons/01_variables/exercice.py
```

`nano` est un éditeur volontairement minimal. Les deux seules touches à retenir
sont affichées en bas de l'écran :

| Touche | Effet |
|---|---|
| `Ctrl + O` puis Entrée | enregistrer |
| `Ctrl + X` | quitter |
| `Ctrl + K` | couper la ligne courante |

Rappel : `Ctrl` est dans la rangée de touches de Termux, ou Volume bas + la
lettre.

Pour l'indentation, la touche **Tab** de la rangée Termux fonctionne dans nano.

Une alternative plus douce si nano te rebute : `pkg install micro`, puis
`micro fichier.py`. Cet éditeur se comporte comme une application normale —
`Ctrl + S` enregistre, `Ctrl + Q` quitte.

## Les autres options, en bref

**Lire sur GitHub, taper dans Termux.** L'application GitHub affiche très bien
les fichiers `.md` de ce dépôt. Garde-la ouverte pour lire les leçons, et
bascule dans Termux pour écrire. Deux applications côte à côte en écran partagé,
si ton téléphone le permet, c'est confortable.

**GitHub Codespaces.** Depuis le navigateur, GitHub peut t'ouvrir un VS Code
complet tournant sur leurs serveurs, avec un terminal. Ça marche sur téléphone,
et c'est bluffant. Il existe un quota gratuit mensuel pour les comptes
personnels — je ne connais pas son montant exact aujourd'hui, vérifie-le avant
de t'y installer, car au-delà c'est facturé.

**Pydroid 3** (Play Store). Un Python avec éditeur et bouton « exécuter »,
pensé pour le mobile. Pratique pour essayer trois lignes tout de suite, moins
adapté à un dossier de projet avec des tests. Un bon bac à sable d'appoint.

**Me demander de lancer les commandes ici.** Je peux exécuter ton code et te
dire ce qui se passe. Sur un dépannage ponctuel, c'est utile. Mais si ça devient
ton mode par défaut, tu auras appris à me faire coder, pas à coder — et le
`verifier.py` perd tout son sens, puisque son intérêt est justement d'être un
juge qui ne dépend pas de moi. Garde ça pour les moments où tu es bloqué.

## Ce à quoi tu peux t'attendre

Les leçons 1 à 5 passent très bien au téléphone : les exercices tiennent en
quelques lignes. La leçon 6 et le projet, où l'on manipule des fichiers et où le
code s'allonge, deviennent nettement plus agréables avec un clavier.

Commence par la leçon 1 dans Termux. Tu sauras en une demi-heure si le confort
te convient, et c'est une réponse plus fiable que tout ce que je peux prévoir
d'ici.
