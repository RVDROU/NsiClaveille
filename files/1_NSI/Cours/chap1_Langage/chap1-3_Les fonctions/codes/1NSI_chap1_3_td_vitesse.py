def vitesse (temps, distance) :         
                                
    '''                        
    Calcul la vitesse moyenne d’un      
    vehicule                        
                                
    arguments :                     
                                
    temps ->  reel positif  (secondes)      
    distance -> reel positif (metres)       
                                
    retour :                        
    reel positif -> vitesse en m/s      
    '''                         
    vit = distance/temps            
                                
    return vit

resultat = vitesse(10,2)