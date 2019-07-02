#importar openbabel
import openbabel
from openbabel import pybel


#pega o arquivo smile.txt e transforma em um module de strings
#o arquivo .txt não pode ter linha em branco no final
with open('smiles.txt', 'r') as file:
	smile = file.read().splitlines();
	#para pegar as linhas com aaa\n usar file.readlines()

#pega os valores do module e le como smile
n = 0
while (n < len(smile)):
	xyz = pybel.readstring('smi', smile[n])
	output = pybel.Outputfile('xyz', 'a_{}.xyz'.format(n), overwrite=True)
	xyz.make3D(forcefield='mmff94', steps=50)
	output.write(xyz)
	n+=1;
