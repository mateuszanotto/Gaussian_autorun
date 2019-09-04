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

	# salva as linhas do .com numa lista
	with open('input/input_{}.com'.format(n), 'r') as file:
		lines = file.readlines()

	# adiciona os inputs do gaussian no .com
	with open('input/input_{}.com'.format(n), 'w') as file:
		lines[0] = '%nprocs=8 \n%mem=16GB \n%chk={path}/chk/moleculeA_{n}.chk \n#opt freq blyp/6-31g(d,p) \n\nmoleculeA_{n} {smi}\n\n'.format(path=path , n=n, smi=smi) # processadores, memoria, chk, input e nome(molecule_No Smile)  \n%chk={}/log/molecule_{}.chk
		lines[1] = '0 1\n' # multiplicidade e carga
		file.writelines(lines) #sobrescreve as linhas 0 e 1 com as infos acima

    # adiciona algo ao fim do arquivo .com
	with open('input/input_{}.com'.format(n), 'a') as file:
 		file.write('\n') # linha em branco (necessario pro input do gaussian)

	# cria um job para cada molecula
	with open('input/job_{}.sh'.format(n), 'w') as file:
		file.write('#!/bin/bash\n\ncd {}/input\ng09 < input_{}.com >  {}/log/moleculeA_{}.log'.format(path, n, path, n))

	subprocess.run('chmod a+x {}/input/job_{}.sh'.format(path, n), shell=True)

	n += 1;

#############
i = 0
while (i < len(Smiles)):
	# checa se o .log tem 0, 1 ou 2 normal terminations
	try:
		with open('{}/log/moleculeA_{}.log'.format(path, i), 'r') as file:
			normterm = str(file.readlines())
			ntcounter = len(list(re.finditer('Normal termination of Gaussian 09', normterm)))
			if ntcounter == 0: # 0 normal termination = erro opt
				print('Molecula {} opt error termination'.format(i));
			if ntcounter == 1: # 1 normal termination = erro freq
				print('Molecula {} freq error termination'.format(i));
			elif ntcounter == 2:
				None # 2 normal termination = normal

	except FileNotFoundError:
		print('Rodando Molecula {}'.format(i)) # aviso no terminal
		subprocess.call('{}/input/job_{}.sh'.format(str(path), i), shell=True) # rodar job se o .log n existir

	i += 1;

#############

#j = 0
#while (j < len(Smiles)):
