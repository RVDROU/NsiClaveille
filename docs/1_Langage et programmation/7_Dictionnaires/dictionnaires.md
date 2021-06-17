Les *dictionnaires*
===================

Un dictonnaire (type dict) est un type construit (données composites)
mutable de la même manière qu’une liste. La principale différence est
que les indices ne sont pas obligatoirement des entiers (0, 1, 2, 3 …)
et peuvent être de type str, float.

Ces indices ne sont pas ordonnés et s’appellent des *clés*. A chaque clé
correspond une valeur.

Ce type de données sera privilégié lors de manipulation de tableau de
données non homogènes (mélangeant des chaînes de caractères et des
entiers).

1.  Construction d’un dictionnaire
    ------------------------------

Un dictionnaire peut être construit à partir d’un dictinnaire vide, noté
{ } et en y ajoutant des entrées avec des affectations de la forme
d\[clé\] = valeur

*&gt;&gt;&gt; dico = {}*

*&gt;&gt;&gt; dico\[‘yes’\] = ‘oui’*

*&gt;&gt;&gt; dico\[‘no’\] = ‘non’*

*&gt;&gt;&gt; dico\[‘and’\] = ‘et’*

*&gt;&gt;&gt; dico\[‘or’\] = ‘ou’*

*&gt;&gt;&gt; dico*

*{‘or’ : ‘ou’, ‘and’ : ‘et’, ‘no’ : ‘non’, ‘yes’ : ‘oui’}*

Il est aussi possible de définir directement entre accolades, l’ensemble
de clés : valeurs séparés par des virgules.

*&gt;&gt;&gt; dico = {‘or’ : ‘ou’, ‘and’ : ‘et’, ‘no’ : ‘non’, ‘yes’ :
‘oui’}*

*&gt;&gt;&gt; dico*

*{‘and’ : ‘et’, ‘or’ : ‘ou’, ‘no’ : ‘non’, ‘yes’ : ‘oui’}*

*Remarque* : L’ordre d’insertion n’est pas important. Le dictionnaire
est affiché en *présentant les clés dans un ordre arbitraire*, qui n’est
ni l’ordre d’insertion, ni l’ordre alphabétique.

1.  Manipulation des dictionnaires
    ------------------------------

<!-- -->

1.  Opérations sur les dictionnaires
    --------------------------------

Des opérateurs spécifiques de filtrage de données existent afin de
comparer deux dictionnaires. Ces opérateurs sont associés à des méthodes
qui donnent accès à l’ensemble des couples clé/valeur (méthode item) ou
plus spécifiquement à l’ensemble des clés (méthode keys) ou des valeurs
(méthode values).

*&gt;&gt;&gt; dico = {‘or’ : ‘ou’, ‘and’ : ‘et’}*

*&gt;&gt;&gt; dico.items()*

*dict\_items(\[(‘or’ : ‘ou’), (‘and’ : ‘et’)\])*

*&gt;&gt;&gt; dico.keys()*

*dict\_keys(\[‘or’,‘and’\])*

*&gt;&gt;&gt; dico.values()*

*dict\_values(\[‘ou’,‘et’\])*

**


