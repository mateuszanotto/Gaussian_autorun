#####################################
#									 #
#									 #
#			mestrado				 #
#									 #
#	mateus m z toledo				 #
######################################

### tentar fazer o xyz virar um input em .com

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
    output = pybel.Outputfile('xyz', 'input/input_{}.com'.format(n), overwrite=True)
    output.write(xyz)

    with open('input/input_{}.com'.format(n), 'r') as file:
        lines = file.readlines()

    with open('input/input_{}.com'.format(n), 'w') as file:
        lines[0] = '%nprocs = 8 \n%mem = 16GB \n%chk=molecule_{}.chk \n# opt freq b3lyp/6-31g(d,p) \n\ninput {}\n\n'.format(n, n)
        lines[1] = '0 1\n'
        file.writelines(lines)

    # adiciona o smile ao fim do arquivo .xyz
    with open('input/input_{}.com'.format(n), 'a') as file:
        file.write("\n")

        n += 1;
