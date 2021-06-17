Les *chaînes de caractères dans Python*
=======================================

Une chaîne de caractères est une structure de ***données composites*** :
une chaîne de caractères est formée de plusieurs valeurs simples que
sont ses différents caractères. Cette structure de données est dîtes
***immutable,*** c’est à dire qu’il n’est pas possible de la modifier
sur place (impossibilité de rajouter ou retirer des caractères). Pour
modifier une chaîne existante, on en extrait les parties appropriées, et
on reconstitue une nouvelle chaîne à l’aide de l’opération de
concaténation.

1.  Déclaration d’une chaîne de caractères
    --------------------------------------

Sous Python, on déclare une chaine de caractères enbordant le texte de
guillemets (simple ou double quote)

*&gt;&gt;&gt;a=’Ceci est une chaine de caracteres’*

*&gt;&gt;&gt;a*

*’Ceci est une chaine de caracteres’*

1.  Accès aux *caractères d’une chaîne de caractères*
    -------------------------------------------------

Puisqu’une chaîne de caractère est une donéne composite, il est possible
d’accéder à chaque caractère la composant par son indice. Cette méthode
d’accès est similaire à celle utilisée dans la manipulation de listes.
L’indice (ou index) du caractère de la chaîne est défini entre crochets.

*&gt;&gt;&gt;a=’Ceci est une chaine de caracteres’*

*&gt;&gt;&gt;a\[0\]*

*‘C’*

*&gt;&gt;&gt;a\[6\]*

*‘s’*

*&gt;&gt;&gt;a\[-1\]*

*‘s’*

### **

1.  Le balayage d’une *chaîne de caractère*
    ---------------------------------------

Le balayage d’une chaîne de caractère consiste à lire successivement
l’ensemble des caractères qu’elle contient afin d’éventuellement opérer
un traitement. Cette opération peut être réalisé avec une boucle for
ayant la liste à balayer comme argument. Dans l’exemple suivant, la
variable i prendra successivement les valeurs contenues dans le tableau.
La boucle for sera donc exécutées 9 fois puisque la chaîne a contient 9
caractères.

1.  Opération sur les *chaînes de caractères*
    -----------------------------------------

<!-- -->


