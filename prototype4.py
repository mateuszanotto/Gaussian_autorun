######################################
#              mestrado              #
#            outubro 2019            #
#       smile -> input gaussian      #
#               patch 0.8            #
#           mateus m z toledo        #
######################################

import openbabel
from openbabel import pybel
import Gaussian_autorun as ga
from pathlib import Path
import os
path = os.getcwd()

## define o caminho até a pasta e o cálculo
name = 'opt'
calc = ['8', #processadores
        '16', #memoria em GB
        '#p opt b3lyp/6-31g(d)'] # calculo


opt = ga.Gaussian_autorun(path, name, calc)
#opt.Inputs()
#opt.Run()
#opt.Error()
opt.test()
mymol = pybel.readstring("smi", "CC")

mol = pybel.Molecule(pybel.readfile("g09", "{}/log/opt_molecule_0.log".format(path)))

print(mol.formula())
print('--------------------------------------------')

## define o caminho até a pasta e o cálculo
name = 'freq' #nome no começo do arquivo
calc = ['8', #processadores
        '16', #memoria em GB
        '#p freq b3lyp/6-31g(d)'] # calculo


freq = ga.Gaussian_autorun(path, name, calc)
#freq.Inputs()
#freq.Run()
#freq.Error()
#freq.test()
freq.test()
