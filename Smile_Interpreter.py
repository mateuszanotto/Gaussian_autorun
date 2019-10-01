from pathlib import Path
import re
import subprocess

class Smile_Interpreter():
    #definicao
    def NormalTerm(self, i):
        path = Path('/home/mateus/github/db_singletoxygen')
        try:
            with open('{}/log/molecule_{}.log'.format(path, i), 'r') as file:
                #transforma o arquivo numa string
                normterm = str(file.readlines())
                #conta os normal terminaiton na string acima
                ntcounter = len(list(re.finditer('Normal termination of Gaussian 09', normterm)))
                return ntcounter
        except FileNotFoundError:
            print('Rodando Molecula {}'.format(i)) # aviso no terminal
            subprocess.call('{}/input/job_{}.sh'.format(str(path), i), shell=True) # rodar job se o .log n existir
