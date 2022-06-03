import mysql.connector as sgbd
import matplotlib.pyplot as plt
import datetime

def filtre10 ( ls ) :
    """ prend en argument une liste ls ( liste de nombres) de longueur n
    renvoie une liste à n éléments.
    """
    res = [ ]
    for k in range(len(ls)) : 
        tot = 0
        for j in range(k-9,k+1):
            if type(ls[j]) is not type(None) : tot +=ls [ j ]
        res .append(tot/10) #
    return res


mydb = sgbd.connect(            
        host="176.181.118.75",
        port = 3306,
        user="tp22_eleve",
        password="eleve",
        database="Noaa2012"
)

mycursor = mydb.cursor()



mycursor. execute(" SELECT Tmax, Tmin, Tavg, Date FROM weather JOIN station ON weather.StationId = station . StationId WHERE CallSign = 'JFK'")
rows = mycursor.fetchall()
lsTmin=[]
lsTmax = []
lsAvg = []
lsTminF10 = []
lsTmaxF10 = []
lsAvgF10 = []
lsDate = []
i = 1
for ligne in rows :
    lsTmax.append(ligne[0])
    lsTmin.append(ligne[1])
    lsAvg.append(ligne[2])
    lsDate .append(datetime.datetime.strptime ( ligne [3], "%Y%m%d"))
lsTminF10 = filtre10(lsTmin)
lsTmaxF10 = filtre10(lsTmax)
lsAvgF10 = filtre10(lsAvg)

fig = plt.figure()        
sub = fig.add_subplot(111) 
sub.plot(lsDate, lsTmaxF10, label='Tmax')
sub.plot(lsDate, lsTminF10, label='Tmin')
sub.plot(lsDate, lsAvgF10, label='Moyenne')  
sub.xaxis_date()
fig .autofmt_xdate()
plt.ylabel ('Température (°)')
plt.legend()               
plt.show()  