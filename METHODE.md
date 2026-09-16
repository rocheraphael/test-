# Coder avec une IA sans arrêter de comprendre

Tu as dit « vibe coding, mais en comprenant ». Ces deux choses tirent dans des
directions opposées, et il vaut mieux le savoir dès le départ.

Le vibe coding, c'est décrire ce qu'on veut et accepter le code produit. C'est
rapide, et parfois c'est exactement le bon outil. Mais il crée une dette
invisible : le jour où le programme casse — et il cassera — tu te retrouves
devant du code que tu n'as jamais compris, à demander à l'IA de réparer une
chose que tu ne sais pas décrire. Beaucoup de débutants tournent en rond des
heures à ce stade.

Ce qui suit est une façon de garder la vitesse sans contracter cette dette.

## La règle du « je peux l'expliquer »

Avant d'ajouter une ligne de code à ton programme, tu dois pouvoir dire à voix
haute ce qu'elle fait. Pas la théorie complète — juste : *cette ligne prend la
liste, la parcourt, et garde les nombres pairs*.

Si tu n'y arrives pas, tu as le droit d'utiliser le code quand même, mais
demande d'abord l'explication. « Explique-moi la ligne 7 comme si je n'avais
jamais vu Python. » C'est une question parfaitement légitime, et c'est
exactement ce pour quoi je suis utile.

## Quatre façons de me poser une question

Toutes ne se valent pas. Par ordre croissant de valeur pour ton apprentissage :

**1. « Écris-moi un programme qui… »**
Tu obtiens du code. Tu n'apprends rien, sauf si tu enchaînes avec des questions.
Utile quand tu veux voir à quoi ressemble une solution complète — à condition de
la disséquer ensuite.

**2. « Voici mon code, il ne marche pas. »**
Mieux. Tu as essayé. Mais ajoute toujours : *et dis-moi pourquoi je me suis
trompé*, sinon tu répares sans comprendre.

**3. « Voici comment je compte m'y prendre : … Est-ce que ça tient debout ? »**
Là tu penses, et je vérifie. C'est le mode le plus rentable. Tu gardes la
conception, je te signale les impasses avant que tu y perdes une heure.

**4. « Pose-moi une question pour vérifier que j'ai compris. »**
Le plus inconfortable, le plus efficace. Tu découvres ce que tu crois savoir.

## Ce qu'il faut me faire faire, sans hésiter

- Expliquer un message d'erreur en français clair.
- Donner trois exemples d'un concept plutôt qu'une définition.
- Relire ton code et te dire ce qui est maladroit — et pourquoi.
- Te fabriquer des exercices supplémentaires sur un point qui résiste.
- Te dire quand tu n'as pas besoin d'apprendre quelque chose maintenant.

## Ce qu'il vaut mieux ne pas me faire faire au début

- Écrire à ta place le cœur d'un exercice que tu es en train de faire.
- Produire d'un coup un programme de 200 lignes dont tu ne lis que la sortie.
- Trancher seul les choix de conception de ton projet : décide, puis soumets.

## Le garde-fou : les tests

Dans ce dépôt, chaque exercice a un fichier de test. C'est important pour une
raison qui dépasse l'exercice : **un test est une vérité qui ne dépend ni de
toi ni de moi.** Je peux me tromper en affirmant que ton code est correct. Le
test, lui, l'exécute.

Prends l'habitude, plus tard, dans tes propres projets : quand tu me demandes du
code, demande aussi de quoi le vérifier. « Écris-moi cette fonction, et écris-moi
trois tests qui prouvent qu'elle marche, dont un cas limite. »

## Quand tu bloques

Dans l'ordre, avant de demander de l'aide :

1. Relis le message d'erreur. En entier. La dernière ligne dit *quoi*, les
   lignes au-dessus disent *où*.
2. Affiche ce que tu ne comprends pas : `print(ma_variable)` juste avant la
   ligne qui casse. Vois si la valeur est celle que tu croyais.
3. Simplifie : retire du code jusqu'à ce que ça marche, puis remets les morceaux
   un par un.

Ces trois réflexes valent plus que n'importe quelle réponse que je pourrais te
donner. Si après ça tu bloques encore, viens me voir — et raconte-moi ce que tu
as déjà essayé. Ça change complètement la qualité de l'aide que je peux
t'apporter.

## Un mot sur le rythme

Une leçon par séance, exercice compris, c'est un bon rythme. Deux, si ça coule.
Jamais six : le quatrième concept d'affilée ne se fixe pas.

Et reviens en arrière sans honte. Relire la leçon 3 en faisant la leçon 5 n'est
pas un échec, c'est la façon normale dont ça rentre.
