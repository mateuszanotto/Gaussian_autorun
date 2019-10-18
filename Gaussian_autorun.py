import openbabel
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

#https://openbabel.org/docs/dev/UseTheLibrary/Python_Pybel.html
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
    #              patch 0.8.1           #          \          /
    #           mateus m z toledo        #           )       /`
    ######################################           /      /`\n\n ''')

    def __init__(self, path, name, calc):
        self.path = path
        self.name = name
        self.calc = calc
        self.normal = []
        self.error = []
        self.smiles = list(pybel.readfile('smi', '{}/smiles.smi'.format(path)))

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
            smi = self.smiles[n]
            smi.make3D(forcefield='mmff94', steps=50)

            try:
                os.mkdir(self.path+"/input")
            except FileExistsError:
                output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
                output.write(smi)
            else:
                output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
                output.write(smi)

            with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'r') as file:
                lines = file.readlines()
            with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'w') as file:
                lines[0] = '''%nprocs={calc[0]}
%mem={calc[1]}GB
%chk={path}/chk/{name}_molecule_{n}.chk
{calc[2]}
\nmolecule_{n} {smi}
0 1'''.format(name=self.name, calc=self.calc, path=self.path , n=n, smi=self.smiles[n])
                lines[-1] += '\n'
                file.writelines(lines)
                file.close()
            with open('input/{name}_job_{n}.sh'.format(name=self.name, n=n), 'w') as file:
                file.write('''#!/bin/bash
cd {path}/input
g09 < {name}_input_{n}.com > {path}/log/{name}_molecule_{n}.log'''.format(name=self.name, path=self.path, n=n))
            subprocess.run('chmod a+x {path}/input/{name}_job_{n}.sh'.format(name=self.name, path=self.path, n=n), shell=True) # cria input.com e job.sh

    def Run(self):
        for n in range(len(self.smiles)):
            try:
                os.mkdir(self.path+"/log")
                os.mkdir(self.path+"/chk")
            except FileExistsError:
                None
            try:
                open('{path}/log/{name}_molecule_{n}.log'.format(path=self.path, name=self.name,  n=n), 'r')
                ### da pra colocar por aqui pra ver se o Smile ta igual
                ### tentar por um SIM ou NÃO
            except FileNotFoundError:
                print('\nRunning {name} calculation - Molecule {n}'.format(name=self.name, n=n)) # aviso no terminal
                subprocess.call('{path}/input/{name}_job_{n}.sh'.format(path=self.path, name=self.name,  n=n), shell=True) # rodar job se o .log n existir
            finally:
                try:
                    open('{path}/log/{name}_molecule_{n}.log'.format(path=self.path, name=self.name,  n=n), 'r')
                    ### da pra colocar por aqui pra ver se o Smile ta igual
                    ### tentar por um SIM ou NÃO
                except FileNotFoundError:
                    print('\nRunning {name} calculation - Molecule {n}'.format(name=self.name, n=n)) # aviso no terminal
                    subprocess.call('{path}/input/{name}_job_{n}.sh'.format(path=self.path, name=self.name,  n=n), shell=True) # rodar job se o .log n existir

    def Error(self):
        for n in range(len(self.smiles)):
            with open('{path}/log/{name}_molecule_{n}.log'.format(path=self.path, name=self.name,  n=n), 'r') as file:
                normterm = str(file.readlines())
                self.normal.append(len(list(re.finditer('Normal termination of Gaussian 09', normterm))))
                self.error.append(len(list(re.finditer('Error termination', normterm))))
                if self.normal==0:
                    print('\nMolecule {n} error termination'.format(n=n))
        if sum(self.normal)!=len(self.normal):
            print('\n- ERROR TERMINATION ON {name} (ﾉ｀□´)ﾉ⌒┻━┻ - \n'.format(name=self.name))
            print('List of {name} Error terminations:'.format(name=self.name))
            for n in range(len(self.smiles)):
                if self.normal[n]==0:
                    print('Molecule {n} ERROR termination'.format(n=n))
            print('\n┬─┬ノ(ಠ_ಠノ)')
        elif sum(self.normal)==len(self.normal):
            print('\n {self} Normal terminated ʕᵔᴥᵔʔ\n '.format(self=self.name)) # mostrar erros e normal terminations

    #def LogRead(self, infos): # lê as infos no .log e salva em um arquivo


    #def LogtoSmi(self):
    #    for n in range(len(self.smiles)):
    #        molecule = readfile('log', '{path}/log/{name}_molecule_{n}.log'.format(path=self.path, name=self.name, n=n))
    #        fps[0] = molecule.calcfp()
    #        fps[1] = self.smile[n].calcfp()
    #        if fps[0] == fps [1]
    #            print('a')
    #        else
    #            None

    def test(self):
        for n in range(len(self.smiles)):
            smi_opt = (pybel.readfile('log', '{path}/log/{name}_molecule_{n}.log'.format(path=self.path, name=self.name, n=n)))
            if str(self.smiles[n]) == str(smi_opt):
                print('igual')
            else:
                print('fail')

    def compare(self, other):
        try:
            self.smiles == other.smiles
            print('Smiles on {name} == Smiles on {other}'.format(name=self.name, other=other.name))
        except:
            raise ValueError('Smiles on {name} != Smiles on {other}'.format(name=self.name, other=other.name))
