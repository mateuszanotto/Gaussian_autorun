import openbabel
#import sys
#print('Python version:{}'.format(sys.version))
from openbabel import pybel
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

class Gaussian_autorun():
    '''This class turn smiles into inputs, runs Gaussian and create an database
    '''
    print('''
    ######################################                         _
    #              mestrado              #        _        ,-.    / )
    #                                    #       ( `.     // /-._/ /
    #            outubro 2019            #        `\ \   /(_/ / / /
    #       smile -> input gaussian      #          ; `-`  (_/ / /
    #                                    #          |       (_/ /
    #               patch 0.8            #          \          /
    #           mateus m z toledo        #           )       /`
    ######################################           /      /`\n\n ''')

    def __init__(self, path, name, calc):
        self.path = path
        self.name = name
        self.calc = calc
        self.normal = []
        self.error = []
        if (path != None):
            with open('{}/smiles.txt'.format(path), 'r') as file:
                self.smiles = file.read().splitlines()

    def __str__(self):
        '''Give a string if the object is printed
        '''
        x='  \n  - Smiles - '
        x+='\n'+str(self.smiles)
        return x

    def Inputs(self):
        '''turn smiles.txt into 3D structures and save in a file
        '''
        for n in range(len(self.smiles)):
            smi = pybel.readstring('smi', self.smiles[n])
            smi.make3D(forcefield='mmff94', steps=50)

            try:
                os.mkdir(self.path+"/input")
            except FileExistsError:
                output = pybel.Outputfile('xyz', 'input/{self}_input_{n}.com'.format(self=self.name, n=n), overwrite=True)
                output.write(smi)
            else:
                output = pybel.Outputfile('xyz', 'input/{self}_input_{n}.com'.format(self=self.name, n=n), overwrite=True)
                output.write(smi)

            with open('input/{self}_input_{n}.com'.format(self=self.name, n=n), 'r') as file:
                lines = file.readlines()
            with open('input/{self}_input_{n}.com'.format(self=self.name, n=n), 'w') as file:
                lines[0] = '''%nprocs={calc[0]}
%mem={calc[1]}GB
%chk={path}/chk/{self}_molecule_{n}.chk
{calc[2]}
\nmolecule_{n} {smi}
\n0 1'''.format(self=self.name, calc=self.calc, path=self.path , n=n, smi=self.smiles[n])
                lines[-1] += '\n'
                file.writelines(lines)
                file.close()
            with open('input/{self}_job_{n}.sh'.format(self=self.name, n=n), 'w') as file:
                file.write('''#!/bin/bash
cd {path}/input
g09 < {self}_input_{n}.com > {path}/log/{self}_molecule_{n}.log'''.format(self=self.name, path=self.path, n=n))
            subprocess.run('chmod a+x {path}/input/{self}_job_{n}.sh'.format(self=self.name, path=self.path, n=n), shell=True) # cria input.com e job.sh

    def Run(self):
        for n in range(len(self.smiles)):
            try:
                os.mkdir(self.path+"/log")
                os.mkdir(self.path+"/chk")
            except FileExistsError:
                try:
                    open('{path}/log/{self}_molecule_{n}.log'.format(path=self.path, self=self.name,  n=n), 'r')
                    ### da pra colocar por aqui pra ver se o Smile ta igual
                    ### tentar por um SIM ou NÃO
                except FileNotFoundError:
                    print('\nRunning {self} calculation - Molecule {n}'.format(self=self.name, n=n)) # aviso no terminal
                    subprocess.call('{path}/input/{self}_job_{n}.sh'.format(path=self.path, self=self.name,  n=n), shell=True) # rodar job se o .log n existir
            else:
                try:
                    open('{path}/log/{self}_molecule_{n}.log'.format(path=self.path, self=self.name,  n=n), 'r')
                    ### da pra colocar por aqui pra ver se o Smile ta igual
                    ### tentar por um SIM ou NÃO
                except FileNotFoundError:
                    print('\nRunning {self} calculation - Molecule {n}'.format(self=self.name, n=n)) # aviso no terminal
                    subprocess.call('{path}/input/{self}_job_{n}.sh'.format(path=self.path, self=self.name,  n=n), shell=True) # rodar job se o .log n existir


    def Error(self):
        for n in range(len(self.smiles)):
            with open('{path}/log/{self}_molecule_{n}.log'.format(path=self.path, self=self.name,  n=n), 'r') as file:
                normterm = str(file.readlines())
                self.normal.append(len(list(re.finditer('Normal termination of Gaussian 09', normterm))))
                self.error.append(len(list(re.finditer('Error termination', normterm))))
                if self.normal==0:
                    print('\nMolecule {n} error termination'.format(n=n))
        if sum(self.error)==0:
            print('\n- No {self} error termination -\n'.format(self=self.name))
#            print('List of {self} Normal terminations: \n'.format(self=self.name)+ str(self.normal))
        elif sum(self.normal)!=len(self.normal):
            print('\n- ERROR TERMINATION ON {self} (ﾉ｀□´)ﾉ⌒┻━┻ - \n'.format(self=self.name))
            print('List of {self} Error terminations:'.format(self=self.name))
            for n in range(len(self.smiles)):
                if self.normal[n]==0:
                    print('Molecule {n} ERROR termination'.format(n=n))
            print('\n┬─┬ノ(ಠ_ಠノ)')
        elif sum(self.normal)==len(self.normal):
            print('\n {self} Normal terminated ʕᵔᴥᵔʔ\n '.format(self=self.name))
