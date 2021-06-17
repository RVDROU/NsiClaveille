Les fonctions
=============

Les fonctions permettent de structurer le code, de le rendre plus
lisible, d’en faciliter la maintenance, en évitant la redondance.
L’utilisation de fonctions fait partie des bonnes pratiques de la
programmation, et est donc très vivement encouragée.

Les fonctions sont des bouts de code d'un programme qui sont exécutés à
chaque fois qu'ils sont appelés. Ainsi, par exemple, vous avez plusieurs
fois besoin d'afficher une liste de choix dans votre console, vous allez
alors écrire ce code une première fois et le marquer comme fonction : on
dit que l'on **définit** une fonction.

1.  Définition d’une fonction
    -------------------------

*\# Code hors fonction*

***def** *nom\_fonction*(argument1, argument2, ...)**:***

* \# Code de la fonction*

***return** *valeur de retour**

*\# Code hors fonction*

1.  Appel d’une fonction
    --------------------

Considérons une fonction double qui multiplie par 2 la somme de deux
nombres passés en paramètre. Une telle fonction s’écrira :

*def double(a,b) :*

*resultat=2\*(a+b)*

*return resultat*

L’appel suivant de la fonction renvoie donc la valeur 24 (24=2\*(4+8))

*&gt;&gt;double(4,8) *

*24*

**

1.  Spécification d’une fonction
    ----------------------------

Une fonction prend des arguments en paramètre, les manipule et renvoie
un résultat. Cette organisation d’un programme permet la réutilisation
et le partage d’algorithmes plus ou moins complexes. Cette notion de
partage oblige les concepteurs de fonctions à décrire la fonction afin
de spécifier :

-   Le nom de l’algorithme,
-   La description des paramètres : quelles variables, quels types ...
-   La description du résultat

Cette spécification est réalisée au début de la fonction par
l’utilisation de **docstrings**.

*def puissance(n,p) :*

*‘’’ Calcul la puissance de p du nombre n*

*arguments : n nombre reel*

*p nombre reel*

*retour : renvoie le resultat de n puissance p*

*‘’’*

*return n\*\*p*

*Remarque* : Les docstrings sont créés en apposant *trois simples cotes*
au début du commentaires et trois autres *décalés d’une tabulation.*

**

1.  Portée des variables
    --------------------

Les variables définies à l’intérieur de la fonction ont une portée
locale c’est à dire qu’elles sont créées à l’appel de la fonction et
détruites à la sortie de la fonction.

*Bien qu’il soit possible d’avoir accès en lecture aux variables
extérieures à la fonction, il est conseillé de passer en argument
l’ensemble des valeurs nécessaires à l’exécution de la fonction.*
