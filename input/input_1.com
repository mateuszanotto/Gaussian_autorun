%nprocs=8 
%mem=16GB 
#opt freq blyp/6-31g(d,p) 

molecule_/home/mateus/github/db_singletoxygen 1

0 1
C          0.95199       -0.07375        0.03127
C          2.47115       -0.09125        0.04932
C          3.00123       -1.08282        1.07122
H          0.58815        0.64512       -0.70959
H          0.55252        0.21347        1.00907
H          0.55252       -1.05976       -0.22635
H          2.84597        0.91121        0.28340
H          2.84597       -0.35544       -0.94563
H          2.66134       -0.82494        2.07926
H          4.09578       -1.08207        1.07046
H          2.66134       -2.09816        0.84384

