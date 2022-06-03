
report = open(REPORT_FILE,"a")

try :
    assert(delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3])
    report.write('    - Test de la fonction "delta" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> La fonction delta n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> jeu de test 1 non validé\n''')
except :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> erreur \n''')
    
try :
    assert(delta([42]) == 42)
    report.write('    - Test de la fonction "delta" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> La fonction delta n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> jeu de test 2 non validé\n''')
except :
    report.write('''    - Test de la fonction "delta" : NONVALIDE -> erreur \n''')

try :
    assert(recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)])
    report.write('    - Test de la fonction "recherche" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "recherche" : NONVALIDE -> La fonction recherche n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "recherche" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "recherche" : NONVALIDE -> erreur \n''')

try :
    assert(calcul(7) == [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    report.write('    - Test de la fonction "calcul" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "calcul" : NONVALIDE -> La fonction calcul n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "calcul" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "calcul" : NONVALIDE -> erreur \n''')

try :
    assert(fibonacci(1) == 1)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 1 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 1 \n''')
    
try :
    assert(fibonacci(2) == 1)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 2 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 2 \n''')
    
try :
    assert(fibonacci(25) == 75025)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 3 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 3 \n''')

try :
    assert(fibonacci(45) == 1134903170)
    report.write('    - Test de la fonction "fibonacci" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> La fonction fibonacci n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> jeu de test 4 non validé\n ''')
except :
    report.write('''    - Test de la fonction "fibonacci" : NONVALIDE -> erreur test 4 \n''')

try :
    assert(rendu_glouton(68,[],0) == [50, 10, 5, 2, 1])
    report.write('    - Test de la fonction "rendu_glouton" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> La fonction rendu_glouton n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> jeu de test 1 non validé\n ''')
except :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> erreur test 1 \n''')
    
try :
    assert(rendu_glouton(291,[],0) == [100, 100, 50, 20, 20, 1])
    report.write('    - Test de la fonction "rendu_glouton" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> La fonction rendu_glouton n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> jeu de test 2 non validé\n ''')
except :
    report.write('''    - Test de la fonction "rendu_glouton" : NONVALIDE -> erreur test 2 \n''')


try :
    assert(pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    report.write('    - Test de la fonction "pascal" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "pascal" : NONVALIDE -> La fonction pascal n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "pascal" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "pascal" : NONVALIDE -> erreur \n''')


unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
try :
    assert(uneCarte.getNom() + " de " + uneCarte.getCouleur() == "8 de coeur")
    report.write('    - Test de la classe "PaquetDeCarte" : VALIDE\n')
except NameError :
    report.write('''    - Test de la classe "PaquetDeCarte" : NONVALIDE -> La classe "PaquetDeCarte" n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la classe "PaquetDeCarte" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la classe "PaquetDeCarte" : NONVALIDE -> erreur \n''')

try :
    assert(tri_bulles([8,36,15,73,94,25]) == [8,15,25,36,73,94])
    report.write('    - Test de la fonction "tri_bulles" : VALIDE\n')
except NameError :
    report.write('''    - Test de la fonction "tri_bulles" : NONVALIDE -> La fonction "tri_bulles" n'existe pas\n''')
except AssertionError :
    report.write('''    - Test de la fonction "tri_bulles" : NONVALIDE -> jeu de test non validé\n ''')
except :
    report.write('''    - Test de la fonction "tri_bulles" : NONVALIDE -> erreur \n''')
    
report.write('\n')
report.close()


