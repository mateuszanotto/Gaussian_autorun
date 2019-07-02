#importar openbabel
import openbabel


# escreve n arquivos com a_n.xyz nomes
n = 1
while n <= 10:

    n_path = '/home/marvin/Desktop/LPTHY/a_{}.xyz'.format(n)
    n_file = open(n_path, 'w')

    title = 'a \n {}'.format(n)
    n_file.write(title)

    n += 1
