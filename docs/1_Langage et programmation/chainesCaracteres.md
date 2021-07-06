# Les chaînes de caractères dans Python

!!! note
	Une chaîne de caractères est une structure de ***données composites***.  
	Une chaîne de caractères est formée de plusieurs valeurs simples que sont ses différents caractères. Cette structure de données est dîtes ***immutable,*** c’est à dire qu’il n’est pas possible de la modifier sur place (impossibilité de rajouter ou retirer des caractères). Pour modifier une chaîne existante, on en extrait les parties appropriées, et on reconstitue une nouvelle chaîne à l’aide de l’opération de concaténation.

## Déclaration d’une chaîne de caractères

Sous Python, on déclare une chaine de caractères enbordant le texte de guillemets (simple ou double quote)
```Python
>>> a = 'Ceci est une chaine de caracteres'
>>> a
'Ceci est une chaine de caracteres'
```
## Accès aux *caractères d’une chaîne de caractères*
Puisqu’une chaîne de caractère est une donéne composite, il est possible d’accéder à chaque caractère la composant par son indice. Cette méthode d’accès est similaire à celle utilisée dans la manipulation de listes.
L’indice (ou index) du caractère de la chaîne est défini entre crochets.

```python
>>> a = 'Ceci est une chaine de caracteres'
>>> a[0]
'C'
>>> a[6]
's'
>>> a[-1]
's'
```

## Le balayage d’une *chaîne de caractère*

Le balayage d’une chaîne de caractère consiste à lire successivement l’ensemble des caractères qu’elle contient afin d’éventuellement opérer un traitement. Cette opération peut être réalisé avec une boucle `for` ayant la liste à balayer comme argument. Dans l’exemple suivant, la variable `i` prendra successivement les valeurs contenues dans le tableau.
La boucle `for` sera donc exécutées 9 fois puisque la chaîne `a` contient 9 caractères.
```python
a = 'Ceci est '		
for i in a :		
	print(i,end=’’)
```
Equivalent à :

```python
a = 'Ceci est '			
for i in range(len(a)):	
	print(a[i],end=’’)	
```
## Opération sur les chaînes de caractères

#### Concaténation et duplication
Les chaînes de caractères supportent l’opérateur `+` de  concaténation, ainsi que l’opérateur `*` pour la duplication :

```python
>>> a = 'Ceci est une '	
>>> b = 'chaine de caracteres'		
>>> a+b						
'Ceci est une chaine de caracteres'
>>>a*2						
'Ceci est une Ceci est une '
```		

#### Longueur d’une chaîne de caractères
La fonction `len()` permet de connaître la longueur d’une chaîne de carctères, c’est-à-dire le nombre de caractères qu’elle contient.

```python
>>> a = 'toi'					
>>> len(a)						
3	
```						

#### Test de présence d’un caractère
La présence d’un caractère peut être testée avec la commande `in`
```python
>>> a = 'Ceci est '				
>>> 'C' in a					
True							
>>> 'E' in a					
False
```							

#### Les tranches (slicing)
Comme pour les listes, il est possible d’extraire une partie d’une chaîne de caractères en utilisant un indiçage construit sur le modèle *[m:n+1]* pour récupérer tous les éléments, du émième au énième (de l’élément m inclus à l’élément n+1 exclu).

```python
>>> a = 'Ceci est '				
>>> a[2:4]						
'ci'							
>>> a[:3]						
'Cec'						
>>> a[:-4]						
'Ceci '
```						

#### Comparaison de chaines
Pour comparer des chaînes de caractères, on utilise les opérateurs `==` et `<=` cette dernière relation comparant deux chaînes pour l’ordre alphabétique.

```python
>>> a = 'Ceci est '			
>>> b = 'Cebi est '			
>>> a == b						
False							
>>> b < a						
True
```							


