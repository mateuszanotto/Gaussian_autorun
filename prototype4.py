######################################
#              mestrado              #
#            outubro 2019            #
#       smile -> input gaussian      #
#               patch 0.8            #
#           mateus m z toledo        #
######################################


import Gaussian_autorun as ga
from pathlib import Path
import os

## define o caminho até a pasta e o cálculo
path = os.getcwd()
typeCalc = 'opt'
calc = ['8', #processadores
        '16', #memoria em GB
        '#p opt b3lyp/6-31g(d)'] # calculo


opt = ga.Gaussian_autorun(path, name, calc)
opt.Inputs()
opt.Run()
opt.Error()

#-----------------------------------------#

## define o caminho até a pasta e o cálculo
path = os.getcwd()
name = 'freq' #nome no começo do arquivo
calc = ['8', #processadores
        '16', #memoria em GB
        '#p freq b3lyp/6-31g(d)'] # calculo


opt = ga.Gaussian_autorun(path, name, calc)
opt.Inputs()
opt.Run()
opt.Error()
