from pathlib import Path
import re

class Smile_Interpreter():
    #definicao
    def NormalTerm(self, i):
        path = Path('/home/mateus/github/db_singletoxygen')
        with open('{}/log/molecule_{}.log'.format(path, i), 'r') as file:
            normterm = str(file.readlines())
            ntcounter = len(list(re.finditer('Normal termination of Gaussian 09', normterm)))
            if ntcounter == 0: # 0 normal termination = erro opt
                print('Molecula {} opt error termination'.format(i));
            if ntcounter == 1: # 1 normal termination = erro freq
                print('Molecula {} freq error termination'.format(i));
            elif ntcounter == 2:
                print('ok {} '.format(i))
