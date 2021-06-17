Typage des données
==================

Tous les langages de programmation permettent de manipuler des valeurs.
Le typage d'une variable consiste à associer à sa variable symbolique un
« type » de donnée, permettant à l'ordinateur de savoir si celle-ci est
de type numérique, textuel, etc. et d'allouer en conséquence des zones
de mémoire de dimension suffisantes pour stocker cette donnée.

Le langage Python effectue un typage dynamique des variables, rendant
cette opération automatique lors de l'exécution du code. Avec certains
langages (C, C++…), le typage doit être effectué statiquement ce qui
demande au programmeur de déclarer expressément le typage de chaque
variable.

1.  Visualisation du typage d’une variable.
    ---------------------------------------

Sous le langage Python, le type d’une variable peut être obtenu avec la
commande* type( )*

**

1.  Principaux types sous Python
    ----------------------------

  ---------------------------------------------------- ---------------------------- -------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- ----------------------
                                                       Nom                          Code                                                                                                                 Description

  Types numériques                                     Integer (Entier)             *int*                                                                                                                Entier compris entre -2 147 483 648 et 2 147 483 647 (codage sur 32 bits soit 4 octets)

  Long integer (Entier long)                           *long*                       long Entier compris entre -∞ et - 2 147 483 647 ou entre 2 147 483 648 et +∞

  Floating point number (Nombre à virgule flottante)   *float*                      Valeur spécifiée avec un point dans le programme (exemple : *a = 2.0*) permettant une approximation de nombre réel

  Types d'objets itérables                             Immuable                     Character string (Chaîne de caractères)                                                                              *str*

  N-uplet (N-uplet)                                    *tuple*                      Tuple de forme
                                                                                    
                                                                                    *(1,2,3,"je suis un tuple",5,3.14159)*

  Muable                                               List (Liste)                 *list*                                                                                                               Liste de forme* \[1,2,3,...\]*

  Dictionary (Dictionnaire)                            *dict*                       Dictionnaire de forme
                                                                                    
                                                                                    *{'Œuf': 1, 'Jambon': 0}*

  Autres                                               Boolean (Valeur booléenne)   *bool*                                                                                                               Type de *True* et de *False* (renvoyés par exemple lors de tests ou d'opérations booléennes)

  Function (fonction)                                  *function*                   Fonction
  ---------------------------------------------------- ---------------------------- -------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------- ----------------------


