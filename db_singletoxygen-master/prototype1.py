#####################################
#									 #
#									 #
#			mestrado				 #
#									 #
#	mateus m z toledo				 #
######################################

# importar openbabel
import openbabel
from openbabel import pybel

# pega o arquivo smile.txt e transforma em um module de strings
# o arquivo .txt não pode ter linha em branco no final
with open('smiles.txt', 'r') as file:
    # para pegar as linhas com aaa\n usar file.readlines()
    Smiles = file.read().splitlines()

# escreve n arquivos onde n eh a quantidade de smiles no arquivo smiles.txt
n = 0
while (n < len(Smiles)):
    # le o smile[n], transforma em smile e salva em xyz
    xyz = pybel.readstring('smi', Smiles[n])
    smi = str(xyz)  # pega o smile atual e faz uma string para salvar depois
    # transforma o smile no xyz e deixa 3d
    xyz.make3D(forcefield='mmff94', steps=50)

    # salva o smile em formato xyz
    output = pybel.Outputfile('xyz', 'xyz/a_{}.xyz'.format(n), overwrite=True)
    output.write(xyz)

    # adiciona o smile ao fim do arquivo .xyz
    with open('xyz/a_{}.xyz'.format(n), 'a') as file:
        fingerprint = str(xyz.calcfp())
        file.write(fingerprint)
        file.write("\n")
        file.write(smi)

        n += 1;

#escreve nos arquivos fora do contador n


i = 0
while (i < len(Smiles)):
    with open('xyz/a_{}.xyz'.format(i), 'a') as file:
        file.write("oi")

        i += 1;
