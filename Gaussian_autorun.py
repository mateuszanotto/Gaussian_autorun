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
                    #print(molecule.molwt) molecule weigth mass
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
#                self.error.append(len(list(re.finditer('Error termination', normterm))))
                if self.normal==0:
                    print('\nMolecule {n} error termination'.format(n=n))
        if sum(self.normal)<len(self.normal):
            print('\n- ERROR TERMINATION ON {name} (ﾉ｀□´)ﾉ⌒┻━┻ - \n'.format(name=self.name))
            print('List of {name} Error terminations:'.format(name=self.name))
            for n in range(len(self.smiles)):
                if self.normal[n]==0:
                    print('Molecule {n} ERROR termination'.format(n=n))
            print('\n┬─┬ノ(ಠ_ಠノ)')
        elif sum(self.normal)==len(self.normal):
            print('\n {self} Normal terminated ʕᵔᴥᵔʔ\n '.format(self=self.name)) # mostrar erros e normal terminations
        elif sum(self.normal)>len(self.normal):
            print('\n {self} Normal terminated ʕᵔᴥᵔʔ *Normal termination > 1 per file*\n '.format(self=self.name)) # mostrar erros e normal terminations


    def LogRead(self): # lê as infos no .log e salva em um arquivo
#    https://docs.python.org/3.1/tutorial/datastructures.html
        for n in range(len(self.smiles)):
            try:
                os.mkdir(self.path+"/xyz")
            except:
                for molecule in pybel.readfile('g09', '{path}/log/opt_molecule_{n}.log'.format(path=self.path, name=self.name, n=n)):
                    #print(molecule.molwt) molecule weigth mass
                    output = pybel.Outputfile('xyz', 'xyz/data_{n}.xyz'.format(n=n), overwrite=True)
                    output.write(molecule)
            finally:
                for molecule in pybel.readfile('g09', '{path}/log/opt_molecule_{n}.log'.format(path=self.path, name=self.name, n=n)):
                    #print(molecule.molwt) molecule weigth mass
                    output = pybel.Outputfile('xyz', 'xyz/data_{n}.xyz'.format(n=n), overwrite=True)
                    output.write(molecule)

            with open('log/{name}_molecule_{n}.log'.format(name=self.name, n=n), 'r') as file:
                lines = file.readlines()
                print (lines)
                if str(self.name) == 'sp':
                    i = 'energy'
                    x=1
                    energy = next(i for i in lines if x>0)
                    print(energy)###






            #with open('xyz/data_{n}.xyz'.format(n=n), 'w') as file:




    def compare(self, other):
        try:
            self.smiles == other.smiles
            print('Smiles on {name} == Smiles on {other}'.format(name=self.name, other=other.name))
        except:
            raise ValueError('Smiles on {name} != Smiles on {other}'.format(name=self.name, other=other.name))

    # def OptInputs(self):
    #     '''turn smiles.smi into 3D structures and save in a file
    #     '''
    #     for n in range(len(self.smiles)):
    #         smi = self.smiles[n]
    #         smi.make3D(forcefield='mmff94', steps=50)
    #
    #         try:
    #             os.mkdir(self.path+"/input")
    #         except FileExistsError:
    #               output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
    #               output.write(smi)
    #         finally:
    #              output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
    #              output.write(smi)
    #
    #         with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'r') as file:
    #             lines = file.readlines()
    #         with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'w') as file:
    #             a = self.header(n)
    #             lines[0] = a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + a[3] + '\n' + a[4] + '\n' + a[5]
    #             lines[-1] += '\n'
    #             file.writelines(lines)
    #             file.close()
    #         with open('input/{name}_job_{n}.sh'.format(name=self.name, n=n), 'w') as file:
    #             file.write(a[6] + '\n' + a[7] + '\n' + a[8] + '\n' + a[9])
    #         subprocess.run('chmod a+x {path}/input/{name}_job_{n}.sh'.format(name=self.name, path=self.path, n=n), shell=True) # cria input.com e job.sh

    # def OtherInputs(self):
    #     '''turn optmized structures into inputs
    #     #https://open-babel.readthedocs.io/en/latest/UseTheLibrary/PythonExamples.html
    #     '''
    #     for n in range(len(self.smiles)):
    #         for molecule in pybel.readfile('g09', '{path}/log/opt_molecule_{n}.log'.format(path=self.path, name=self.name, n=n)):
    #             #print(molecule.molwt) molecule weigth mass
    #             output = pybel.Outputfile('xyz', 'input/{name}_input_{n}.com'.format(name=self.name, n=n), overwrite=True)
    #             output.write(molecule)
    #
    #         with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'r') as file:
    #             lines = file.readlines()
    #         with open('input/{name}_input_{n}.com'.format(name=self.name, n=n), 'w') as file:
    #             a = self.header(n)
    #             lines[1] = '\n'
    #             lines[0] = a[0] + '\n' + a[1] + '\n' + a[2] + '\n' + a[3] + '\n' + a[4] + '\n' + a[5]
    #             lines[-1] += '\n'
    #             file.writelines(lines)
    #             file.close()
    #
    #         with open('input/{name}_job_{n}.sh'.format(name=self.name, n=n), 'w') as file:
    #             file.write(a[6] + '\n' + a[7] + '\n' + a[8] + '\n' + a[9])
    #         subprocess.run('chmod a+x {path}/input/{name}_job_{n}.sh'.format(name=self.name, path=self.path, n=n), shell=True) # cria input.com e job.sh
