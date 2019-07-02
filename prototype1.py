#importar openbabel
import openbabel
from openbabel import pybel


#pega o arquivo smile.txt e transforma em um module de strings com as linhas
#aaa
#bbb
#smile = ['aaa', 'bbb']
with open('smiles.smi', 'r') as file:
	smile = file.read().splitlines();
	#para pegar as linhas com aaa\n usar file.readlines()

#pega os valores do module e le como smile
n = 0
while (n < len(smile)):
	xyz = pybel.readstring("smi", smile[n])
	output = pybel.Outputfile("xyz", 'a_{}.xyz'.format(n), overwrite=False)
	xyz.make3D(forcefield='mmff94', steps=50)
	output.write(xyz)
	n+=1;

# escreve n arquivos com a_n.xyz nomes
#n = 1
#while n <= 10:

	#caminho ate a pasta onde ficara o arquivo
#	path = '/home/marvin/Desktop/LPTHY/a_{}.xyz'.format(n)

	#abrir o arquivo especificado e escrever
#	mymol = open(path, 'w')

	#colocar infos que quer digitar no arquivo
#	write = 'a \n {}'.format(n)

	#digitar a variavel write no arquivo
#	mymol.write(write)

	#aumentar o contador em 1
#	n += 1
