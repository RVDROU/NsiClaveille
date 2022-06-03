'''
Créé le 14/03/22 par Rv
Programme de test automatique de fichier élèves provenant de Moodle.
Les répertoires élèves doivent être placés dans le répertoire courant.

Jeu de test défini dans 'test_set.py'
Commande de correction automatique : test_files('test_set.py', 'report.txt')

'''

import os, pathlib

def hide_space(name) :
    output = ''
    for l in name :
        if l == ' ' :
            output += r'\\'
    return output

def load_test(host, test, report_file) :

     try :    
         test_set = open(test,"r").read()
         f = open(host, 'a')
     except :
         return False
     f.write('\n')
     f.write('REPORT_FILE = "' + report_file + '"')
     f.write(test_set)
     return True

def test_files(test_file, report_file) :
    ''' test_file : str
        report : report file (str)
    '''

    lst_files = os.listdir()
    if report_file in lst_files :
        os.remove(report_file)
    
    lst_dir = [d for d in lst_files if os.path.isdir(d)]
    for directory in lst_dir :
        report = open(report_file,"a")
        name = directory.split('_')[0]
        report.write('\n')
        report.write('\n')
        report.write('- Rapport de test du programme de ' + name +'\n')
        report.write('-----------------------------------------------------------------\n')
        report.close()
        
        student_files = os.listdir('./'+directory)
        if len(student_files) != 1 :
            report.write('Plusieurs fichiers dans le dossier')
            break
        else :
            file = os.path.join('./' ,directory,student_files[0])
            load_test(file, test_file, 'report.txt')
            
            os.system('python3 '+ repr(file))

    print('------------ Test terminé ----------')
    




        

    
    
