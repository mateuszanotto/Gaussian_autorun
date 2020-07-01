import openbabel as ob
import sys
#print('Python version:{}'.format(sys.version))
from openbabel import pybel #[N.M. O’Boyle, C. Morley and G.R. Hutchison. Pybel: a Python wrapper for the OpenBabel cheminformatics toolkit. Chem. Cent. J. 2008, 2, 5.]
from pathlib import Path
import subprocess
import re
import os
#import scipy as sp
#print('SciPy version:{}'.format(sp.__version__))
#import numpy as np
#print('numpy version:{}'.format(np.__version__))
#import pandas as pd
#print('pandas version:{}'.format(pd.__version__))

'''https://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html'''

class Gaussian_autorun():
    '''This class turn smiles into inputs, runs Gaussian and create an database
    '''
    print('''
    ######################################                         _
    #          Gaussian_autorun          #        _        ,-.    / )
    #                                    #       ( `.     // /-._/ /
    #            outubro 2019            #        `\ \   /(_/ / / /
    #       smile -> input gaussian      #          ; `-`  (_/ / /
    #                                    #          |       (_/ /
    #              patch 0.8.2           #          \          /
    #           mateus m z toledo        #           )       /`
    ######################################           /      /`\n\n ''')

    def __init__(self, path, name, calc):
        self.path = path
        self.name = name
        self.calc = calc
        self.normal = []
        self.error = []
        self.smiles = list(pybel.readfile('smi', '{}/smiles.smi'.format(path)))
        self.charge = list()

    def output(self, n):
        self.output = ('',
        '',
        '',
        ''
        )
        a = self.output
        del self.output
        return a

    def numb(self, n):
        with open('{}/smiles.smi'.format(self.path)) as f:
            lines = f.readlines()
            num = lines[n].split()
            charges = int(num[-2])
            multi = int(num[-1])
        return charges, multi

    def header(self, n):
        '''
        Define o cabeçalho do input do Gaussian09 conforme os parametros passados no calc
        '''
        self.header = (('%nprocs={calc[0]}'.format(calc=self.calc)  + '\n'),
        ('%mem={calc[1]}GB'.format(calc=self.calc) + '\n'),
        ('%chk={path}/chk/{name}_molecule_{n}.chk'.format(name=self.name, path=self.path , n=n)  + '\n'),
        (self.calc[2])  + '\n',
        ('\nmolecule_{n} {smi}'.format(n=n, smi=self.smiles[n])  + '\n'),
        ('{charge} {multiplicidade}'.format(charge=self.numb(n)[0], multiplicidade=self.numb(n)[1])),
        ('#!/bin/bash'),
        ('cd {path}/input'.format(path=self.path)),
        ('g09 < {name}_input_{n}.com > {path}/log/{name}_molecule_{n}.log &&'.format(name=self.name, path=self.path, n=n)),
        ('formchk {path}/chk/{name}_molecule_{n}.chk && rm {path}/chk/{name}_molecule_{n}.chk'.format(name=self.name, path=self.path, n=n)))
        a = self.header
        del self.header
        return a

    def __str__(self):
        '''Give a string if the object is printed
        '''
        x='  \n  - Smiles - '
        x+='\n'+str(self.smiles)
        return x

    def Inputs(self):
        '''turn smiles.smi into 3D structures and save in a file
        '''

        for n in range(len(self.smiles)):
            word = 'opt' #ve se tem opt no input e calcula puxando do smile
            if word in self.calc[2].lower().split():
                smi = self.smiles[n]
                smi.make3D(forcefield='mmff94', steps=50)

                try:
                    os.mkdir(self.path+"/input")
                except:
                    output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
                    output.write(smi)
                finally:
                    output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
                    output.write(smi)

            else:
                for molecule in pybel.readfile('g09', '{path}/log/opt_molecule_{n}.log'.format(path=self.path, name=self.name, n=n)):
                    output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
                    output.write(molecule)

            with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'r') as file:
                lines = file.readlines()
            with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'w') as file:
                a = self.header(n)
                lines[1] = '\n'
                for i in range(0,6):
                        lines[0] += a[i]
                lines[-1] += '\n'
                file.writelines(lines)
                file.close()
            with open('input/{name}_job_{n}.sh'.format(name=self.name, n=n), 'w') as file:
                file.write(a[6] + '\n' + a[7] + '\n' + a[8] + '\n' + a[9])
            subprocess.run('chmod a+x {path}/input/{name}_job_{n}.sh'.format(name=self.name, path=self.path, n=n), shell=True) # cria input.com e job.sh
