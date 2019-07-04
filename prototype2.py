######################################
#              mestrado              #
#             julho 2019             #
#       smile -> input gaussian      #
#                                    #
#           mateus m z toledo        #
######################################


# importar openbabel
import openbabel
from openbabel import pybel

# transforma cada linha do smiles.txt num item de uma lista. O arquivo smiles.txt NÃO pode ter linha em branco no final
with open('smiles.txt', 'r') as file:
	Smiles = file.read().splitlines() # para pegar as linhas com 'aaa\n' usar file.readlines()

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
		lines[0] = '%nprocs=8 \n%mem=16GB \n%chk=molecule_{}.chk \n#opt freq b3lyp/6-31g(d,p) \n\ninput {}\n\n'.format(n, n) # processadores, memoria, chk, input e nome
		lines[1] = '0 1\n' # multiplicidade e carga
		file.writelines(lines) #sobrescreve as linhas 0 e 1 com as infos acima

    # adiciona algo ao fim do arquivo .com
	with open('input/input_{}.com'.format(n), 'a') as file:
 		file.write("\n") # linha em branco (necessário pro input do gaussian)

	n += 1;
