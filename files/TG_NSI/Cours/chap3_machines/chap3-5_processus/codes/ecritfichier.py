from os import getpid
pid = str(getpid())
with open ('test.txt','w') as file :
    for i in range(100000) :
        file.write('['+pid+'] : ' + str(i) +'\n')
        file.flush()