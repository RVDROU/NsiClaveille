def temps_en_secondes(h, m, s, ms) :
    '''Converti en seconde une heure
    donnée en heure/minutes/secondes
    '''
    return h*3600 + m*60 + s + ms/1000

def distance(tar, tdep) :
    '''Calcul la distance à partir d'un temps d'arrivée
    et un temps de départ
    '''
    return 300000*(tar-tdep)

def decimale_a_dms(val) :
    ''' Converti les données decimale en dms
    val : entier
    Retour : degrés, minutes, secones
    Rappel : 1 degré = 60 minutes = 3600 secondes
    '''
    deg = val//1   # deg : valeur entière de val
    minutes = (val - deg)*60 # minutes : decimale de val fois 60
    secondes = (minutes - minutes//1)*60
    return val // 1, minutes //1 , secondes //1
    
def dms_a_decimale(deg,minute,sec):
    ''' Converti les données dms en decimale
    deg, minute,sec : entiers
    Rappel : 1 degré = 60 minutes = 3600 secondes
    '''
    deg_minute = minute/60
    deg_sec = sec/3600
    total = deg + deg_minute + deg_sec
    return total