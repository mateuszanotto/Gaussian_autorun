%nprocs=8 
%mem=16GB 
#opt freq blyp/6-31g(d,p) 

molecule_/home/mateus/github/db_singletoxygen 0

0 1
C          1.12265       -0.03899       -0.05879
C          2.32296       -0.03899       -0.05879
H          0.05685       -0.03899       -0.05879
H          3.38876       -0.03899       -0.05879

