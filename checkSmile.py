######################################
#              mestrado              #
#             julho 2019             #
#       smile -> input gaussian      #
#               patch 0.1            #
#           mateus m z toledo        #
######################################

# importar openbabel
import openbabel
from openbabel import pybel
from pathlib import Path
import subprocess
import re

# transforma cada linha do smiles.txt num item de uma lista. O arquivo smiles.txt NAO pode ter linha em branco no final
with open('smiles.txt', 'r') as file:
	Smiles = file.read().splitlines() # para pegar as linhas com 'aaa\n' usar file.readlines()

# Define o caminho ate o script
path = Path('/home/mateus/github/db_singletoxygen')

# escreve n arquivos onde n eh a quantidade de smiles no arquivo smiles.txt
n = 0
while (n < len(Smiles)):
	smibabel = pybel.readstring('smi', Smiles[n]) # transforma o Smiles[n] em um smile compativel com babel
	smi = str(smibabel)  # pega o smile e faz uma string para salvar depois
	smibabel.make3D(forcefield='mmff94', steps=50) # deixa o smile 3d

   	 # salva a molecula 3d em formato xyz
	output = pybel.Outputfile('xyz', 'input/input_{}.com'.format(n), overwrite=True)
	output.write(smibabel)

	log = readfile("log", "molecule_{}".format(n)).next()
	new_Smi = pybel.log('smi')
	newsmi = str(new_Smi)
	print(newsmi)

	if smi == newsmi
		print('ERRO: smile da molécula{} diferente do input'.format(n))
	else
		none

	n += 1;
