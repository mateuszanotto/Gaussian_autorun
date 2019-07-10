%nprocs=8 
%mem=16GB 
#opt freq blyp/6-31g(d,p) 

molecule_/home/mateus/github/db_singletoxygen 2

0 1
C          1.10958       -0.00398       -0.02286
C          2.44537       -0.00398       -0.02286
H          0.54971       -0.65698       -0.68500
H          0.54971        0.64902        0.63928
H          3.00523       -0.65698       -0.68500
H          3.00523        0.64902        0.63928

