# db_singletoxygen

Este projeto é dedicado a criação de um banco de dados contendo informações teóricas (calculadas) de fotossensibilizadores e informações experimentais com foco no rendimento de oxigênio singleto

# é necessário mudar o Path no prototype3.py

# install_pybel
instruções para instalar o openbabel com python3 no linux

0.1 tentar via pip
> pip install openbabel

1. instalar Anaconta python3.7 - https://www.anaconda.com/distribution/#download-section
> bash Anaconda3-2019.03-Linux-86x_64.sh

2. instalar cmake, lxml, swig
> conda install cmake lxml swig
\n > export PATH=~/anaconda3/bin:$PATH

3. Baixar openbabel 2.5.x - github - https://github.com/openbabel

4. Descompactar openbabel e compilar

> cd /openbabel-master
> mkdir build
> cd build
> cmake .. -DPYTHON_BINDINGS=ON -DRUN_SWIG=ON -DCMAKE_INSTALL_PREFIX=~/anaconda3 -DPYTHON_INCLUDE_DIR=~/anaconda3/include/python3.7m/ -DCMAKE_LIBRARY_PATH=~/anaconda3/lib -DSWIG_DIR=~/anaconda3/share/swig/3.0.12/ -DSWIG_EXECUTABLE=~/anaconda3/bin/swig -DPYTHON_LIBRARY=~/anaconda3/lib/libpython3.7m.so
> make && make install
