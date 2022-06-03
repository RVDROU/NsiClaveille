class Noeud():
    def __init__(self, v):
        self.ag = None
        self.ad = None
        self.v = v

    def insere(self, v):
        n = self
        est_insere = False
        while not est_insere :
            if v == n.v:
                est_insere = True
            elif v < n.v:
                if n.ag != None:
                    n = n.ag
                else:
                    n.ag = Noeud(v)
                    est_insere = True
            else:
                if n.ad != None:
                    n = n.ad
                else:
                    n.ad = Noeud(v)
                    est_insere = True

    def insere_tout(self, vals):
        for v in vals:
            self.insere(v)
            
    def rechercher_ver1(self, v) :
        ''' Version récursive'''
        dans_sag = False
        dans_sad = False
        dans_noeud = False
        if self.v == v : dans_noeud = True
        if self.ag != None : dans_sag = self.ag.rechercher_ver1(v)
        if self.ad != None : dans_sad = self.ad.rechercher_ver1(v)
        return dans_sag or dans_sad or dans_noeud
    
    def rechercher_ver2(self, v) :
        ''' Version itérative'''
        n = self
        est_dans = False
        fin = False
        while not (est_dans or fin):
            if v == n.v:
                est_dans = True
            elif v < n.v:
                if n.ag != None:
                    n = n.ag
                else :
                    fin = True
                
            else:
                if n.ad != None:
                    n = n.ad
                else:
                    fin = True
        return est_dans
    
    
racine = Noeud(18)
#racine.insere_tout([12, 13, 15, 16, 19, 21, 32, 23])
racine.insere_tout([15,13,12,16,23,19,21,32])
racine.insere(19)