Les opérations Booléennes
=========================

Les fonctions booléennes sont utilisées partout : dans les langages de
programmation, en architecture des ordinateurs, dans certains
algorithmes cryptographiques… Nous nous concentrons dans ce chapitre sur
les opérations NON, ET et OU qui permettent d’exprimer toutes les
autres.

1.  Expression des opérations Booléennes
    ------------------------------------

Comme les opérations d’une variable réelle, les opérations booléennes
peuvent s’exprimer de manière symbolique : l’expression X.y+x.z est
bâtie sur le même modèle que l’expression (sin(x) × y) + (x × z), sauf
que les variables x, y et z y représentent des booléens et non des
nombres réels.

Contrairement aux fonctions d’une variable réelle, ces fonctions ne
peuvent pas s’exprimer par des courbes. Néanmoins, elles peuvent
s’exprimer par des tables car, à la différence des nombres réels, les
booléens sont en nombre fini.

### Les opérations Booléennes NON, ET, OU

  ----------- ------------ ----------------- ------------------------------------------------------------
  Opérateur   Expression   Table de vérité   Commentaire

  NON         s=A                            s est l’inverse de a
                                             
              s = non a                      

  ET          s = a . b                      s est vrai si les deux propositions d’entrée sont vraies
                                             
              s = a et b                     

  OU          s = a + b                      s est vraie si au moins une proposition d’entrée est vraie
                                             
              s = a ou b                     
  ----------- ------------ ----------------- ------------------------------------------------------------

### Propriétés des opérations Booléennes

  ----------------- --------------- --------------------------- ------------------------------------
  Complémentarité   Commutativité   Associativité               Distributivité

  A + a = 1         a + b = b + a   a + ( b + c ) = a + b + c   a . ( b + c ) = a . b + a . c
                                                                
  a . A = 0         a . b = b . a   a . ( b . c ) = a . b . c   a + ( b . c ) = (a + b ) . (a + c)
                                                                
  \_\_                                                          
                                                                
  A = a                                                         
  ----------------- --------------- --------------------------- ------------------------------------

1.  Opérations Booléennes sous Python
    ---------------------------------

### Opérations Booléennes

Les opérations Booléennes NON, ET, OU sont définies par les instructions
suivantes :

  ---------- ----------- ------------ --------------------------------------
  Priorité   Opérateur   Expression   Résultat
  Haute      NON         *not x*      Si x est faux alors True sinon False
  ↓          ET          *x and y*    Si x est vrai, alors y sinon False
  Faible     OU          *x or y*     Si x est faux, alors y sinon True
  ---------- ----------- ------------ --------------------------------------

Lorsque Python évalue une expression booléenne, il le fait de façon
**paresseuse**. C’est à dire que si la partie gauche d’un or est vraie,
il n’évalue pas la partie droite. De même si la partie gauche d’un and
est fausse, la partie droite n’est pas évaluée. Cela permet d’écrire les
choses suivantes :

> *&gt;&gt;&gt; x=0*

> *&gt;&gt;&gt; x==0 or 1/x&lt;1*

> *True*

> *&gt;&gt;&gt; x!=0 and 1/x&lt;1*

> *False*

Si la division 1/x était évaluée, il y aurait une erreur, puisqu’on le
peut pas diviser par 0. Mais dans les deux cas, l’évaluation n’est pas
faite puisque le résultat de l’expression a déjà pu être déterminée avec
la partie gauche.

### Opérations Booléennes bit à bit des nombres entiers

Les opérations bit à bit ne sont pertinentes que sur les nombres entiers
(types integer).

  ---------------- -----------------------------------
  Expression       Résultat
  *x | y*          OU logique effectué bit à bit
  *x \^ y*         OU Exclusif effectué bit à bit
  *x & y*          ET logique effectué bit à bit
  *x &lt;&lt; n*   x décalé vers la gauche de n bits
  *x &gt;&gt; n*   x décalé vers la droite de n bits
  *\~ x *          Inversion des bits de x
  ---------------- -----------------------------------

> *&gt;&gt;&gt; 9 | 2 \#1001 OU 0011 = 1011 (11)*

> *11*

> *&gt;&gt;&gt; 3 &lt;&lt; 2 \# 0011 (3) décalé de 2 donne 1100 (12)*

> *12*
