######################################
#              mestrado              #
#            outubro 2019            #
#       smile -> input gaussian      #
#               patch 0.8            #
#           mateus m z toledo        #
######################################

import openbabel as ob
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
opt.OptInputs() #cria o arquivo a partir do smile e otimiza, NÃO usar OtherInputs()
opt.Run() #so funciona se não tiver .log
opt.Error()

print('==============================')

name = 'freq' #nome no começo do arquivo
calc = ['8', #processadores
        '16', #memoria em GB
        '#p freq b3lyp/6-31g(d)'] # calculo


freq = ga.Gaussian_autorun(path, name, calc)
freq.OtherInputs() #cria o arquivo a partir da estrutura otimizada, NÃO usar OptInputs()
freq.Run()
freq.Error()

print('==============================')

name = 'sp' #nome no começo do arquivo
calc = ['8', #processadores
        '16', #memoria em GB
        '#p sp mp2/6-31g(d)'] # calculo


sp = ga.Gaussian_autorun(path, name, calc)
sp.OtherInputs() #cria o arquivo a partir da estrutura otimizada, NÃO usar OptInputs()
sp.Run()
sp.Error()
