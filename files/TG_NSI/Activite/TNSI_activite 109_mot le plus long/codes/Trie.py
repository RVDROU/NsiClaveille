class Trie:
    def __init__(self, letter=None):
        self.letter = str(letter)
        self.end = False
        self.node = {} # au début, l'arbre est vide

    def __getitem__(self, letter : str) -> str:
        return self.node.get(letter)
    
    def getLetter(self) -> str:
        return self.letter

    def isWordEnd(self) -> bool:
        return self.end    
        
    def setWordEnd(self):
        self.end = True
        
    def addBranch(self, branch : object):
        self.node[branch.getLetter()]=branch
        
    def makeTrie(self, words : list) -> object:
        ''' crée un trie à partir d'une liste de mots '''
        for word in words:
            node = self
            # on se place au début de l'arbre
            word = word.rstrip()
            for letter in word:
                if node[letter] == None:
                    node.addBranch(Trie(letter))
                node = node[letter] # on avance dans l'arbre
            node.setWordEnd()
        return self

    def inTrie(self, word : str) -> bool:
        node = self
        # on se place au début de l'arbre
        for letter in word:
            if node[letter] != None :
                node = node[letter]
            else:
                return False
        return node.isWordEnd()