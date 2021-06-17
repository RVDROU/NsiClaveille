Les intéractions utilisateur (entrées/sorties)
==============================================

Dans l’exécution d’un programme, il est fréquent que l’utilisateur ait
besoin de saisir des informations.

Les fonctions particulières print() et input() permettent d’intéragir
avec l’utilisateur.

1.  La fonction print()
    -------------------

La fonction print() sert à afficher du texte et/ou le contenu d’une
variable.

* &gt;&gt;&gt;print(‘Bienvenue au cours de NSI.’)*

* Bienvenue au cours de NSI.*

* &gt;&gt;&gt;prenom=’Boris’*

* &gt;&gt;&gt;print(‘Bonjour’, prenom,’, bienvenue au cours de NSI.’) *

* Bonjour Boris, bienvenue au cours de NSI.*

**

### Remarques

Pour afficher plusieurs données avec la fonction print(), il suffit de
les séparer avec des virgules.

La fonction print() effectue un retour à la ligne après l’affichage du
texte. Ce retour à la ligne peut être inhibé avec le paramètre end=’’.

  ------------------------ --------- --------
  *for i in range(3) : *   affiche   *0 *
                                     
  * print(i) *                       *1 *
                                     
                                     *2 *

  *for i in range(3) : *   affiche   *012 *
                                     
  *print(i,end=’’) *                 
  ------------------------ --------- --------

**

1.  La fonction input()
    -------------------

La fonction input() permet des intéraction avec l’utilisateur : elle va
stopper l’exécution du programme et attendre que l’utilisateur saisisse
une donnée. Le programme reprend lorsque l’utilisateur appuie sur la
touche ENTREE. La fonction renvoie alors le texte saisi par
l’utilisateur.

L’instruction suivante aura pour effet d’ouvrir une zone de saisie dans
laquelle l’utilisateur pourra entrer une valeur. Cette valeur sera
affectée à la variable nom.

* &gt;&gt;&gt;nom=input(‘Quel est votre nom ?’) *

### Remarque

La valeur renvoyée par la fonction input() est une chaîne de caractère
(type ‘str’). Pour obtenir un nombre entier, il faudra saisir :

* &gt;&gt;&gt;age=int(input(‘Quel est votre age ?’)) *
