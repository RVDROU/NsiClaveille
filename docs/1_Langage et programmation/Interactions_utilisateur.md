# Les intéractions utilisateur (entrées/sorties)


Dans l’exécution d’un programme, il est fréquent que l’utilisateur ait besoin de saisir des informations.

Les fonctions particulières `print()` et `input()` permettent d’intéragir avec l’utilisateur.

### La fonction `print()`

La fonction `print()` sert à afficher du texte et/ou le contenu d’une variable.

```
>>> print('Bienvenue au cours de NSI.')
Bienvenue au cours de NSI.
>>> prenom=’Boris’
>>> print(‘Bonjour’, prenom,’, bienvenue au cours de NSI.’)
Bonjour Boris, bienvenue au cours de NSI.
```

__Remarques__

Pour afficher plusieurs données avec la fonction print(), il suffit de les séparer avec des virgules.

La fonction `print()` effectue un retour à la ligne après l’affichage du texte. Ce retour à la ligne peut être inhibé avec le paramètre `end=''`.
```python
for i in range(3) :                                       
  print(i)
```
_Affiche_
```
0
1
2
```
------------------------
```python
for i in range(3) :                                       
  print(i,end='')
```
_Affiche_
```
012
```
                                     
### La fonction input()

La fonction `input()` permet des intéraction avec l’utilisateur : elle va stopper l’exécution du programme et attendre que l’utilisateur saisisse une donnée. Le  programme reprend lorsque l’utilisateur appuie sur la touche __ENTREE__. La fonction renvoie alors le texte saisi par l’utilisateur.

L’instruction suivante aura pour effet d’ouvrir une zone de saisie dans laquelle l’utilisateur pourra entrer une valeur. Cette valeur sera affectée à la variable nom.

```python
nom=input('Quel est votre nom ?')
```

__Remarque__

La valeur renvoyée par la fonction input() est une chaîne de caractère (type __str__). Pour obtenir un nombre entier, il faudra saisir :

```python
age=int(input(‘'Quel est votre age ?')) 
```