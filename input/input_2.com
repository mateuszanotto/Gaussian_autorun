%nprocs=8 
%mem=16GB 
%chk=/home/mateus/github/db_singletoxygen/chk/molecule_2.chk 
#opt freq b3lyp/6-31g(d) 

molecule_2 C#C	

0 1
C          1.07006        0.08187       -0.05443
C          2.27036        0.08187       -0.05443
H          0.00426        0.08187       -0.05443
H          3.33617        0.08187       -0.05443

