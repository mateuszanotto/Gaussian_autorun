%nprocs=8 
%mem=16GB 
%chk=/home/mateus/github/db_singletoxygen/chk/molecule_0.chk 
#opt freq b3lyp/6-31g(d) 

molecule_0 C=C	

0 1
C          0.94587        0.00818       -0.07429
C          2.28166        0.00818       -0.07429
H          0.38601        0.90925        0.15571
H          0.38601       -0.89290       -0.30429
H          2.84152        0.90925        0.15571
H          2.84152       -0.89290       -0.30429

