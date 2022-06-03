import Trie as trie


def test_Trie() :
    t = trie.arbreTrie()
    assert t.get_lettre() == 'None' , 'Noeud vide : Méthode get_lettre ou constructeur : HS'
    assert t.liste_suivants() == [] , 'Noeud vide : Méthode liste_suivants : HS'
    assert t.get_suivant('') == None , 'Noeud vide : Méthode get_suivant : HS'
    assert t.est_fin_mot() == False , 'Noeud vide : Méthode est_mot_fin : HS'
    t.set_fin_mot()
    assert t.est_fin_mot() == True , 'Noeud vide : Méthode mot_fin : HS'
    t.ajout_noeud('a')
    assert t.get_lettre() == 'None' , '1 noeud ajouté : Méthode get_lettre ou constructeur : HS'
    assert t.liste_suivants() == ['a'] , '1 noeud ajouté : Méthode liste_suivants : HS'
    assert type(t.get_suivant('a')) == type(t) , '1 noeud ajouté : Méthode get_suivant : HS'
    print('Test des méthodes isolées : Ok')
    t = trie.arbreTrie()
    t.construire(['abcd', 'azerty'])
    assert t.liste_suivants() == ['a'] , 'Erreur de construction du trie'
    assert t.get_suivant('a').liste_suivants() == ['b','z'], 'Erreur de construction du trie'
    for mot in [('abcd', True), ('azerty', True),('rtyaze', False), ('azert', False), ('azertyy', False),\
                ('abc', False), ('abcde', False)] :
        assert t.est_dans_arbre(mot[0]) == mot[1] , 'Erreur de recherche dans Trie pour :'+mot[0]
        
    print ('Test de construction et de recherche : Ok')
    print ('*******************************************************************')
    print ('**                                                               **')
    print ('**                        Test VALIDE                            **')
    print ('**                                                               **')    
    print ('*******************************************************************')    
    