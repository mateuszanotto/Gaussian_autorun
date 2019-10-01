%nprocs=8 
%mem=16GB 
%chk=/home/mateus/github/db_singletoxygen/chk/molecule_8.chk 
#opt freq blyp/6-31g(d,p) 

molecule_8 Cc1cc(=O)oc2c1ccc1sc(C)c(C)c21	


0 1
C          0.96385       -0.01986        0.05928
C          2.46438       -0.02062        0.06036
C          3.17802        1.11148        0.06121
C          4.64612        1.13140        0.06976
O          5.25215        2.20144        0.07323
O          5.29234       -0.09725        0.07573
C          4.58230       -1.33501        0.07163
C          3.17414       -1.30318        0.06271
C          2.46479       -2.50242        0.05631
C          3.11784       -3.72062        0.05993
C          4.51403       -3.73294        0.07060
S          5.43521       -5.15823        0.07746
C          6.89557       -4.29852        0.08914
C          8.13546       -5.12243        0.09910
C          6.71378       -2.91946        0.08767
C          7.82797       -1.91491        0.09671
C          5.29309       -2.57366        0.07671
H          0.55104        0.99199        0.05993
H          0.58043       -0.53157        0.95003
H          0.58048       -0.53093       -0.83170
H          2.69948        2.08439        0.05806
H          1.38008       -2.53383        0.04822
H          2.55959       -4.65163        0.05521
H          7.90011       -6.19516        0.09724
H          8.71991       -4.92180        0.99987
H          8.73425       -4.92180       -0.79218
H          8.80924       -2.40135        0.10453
H          7.76925       -1.27803        0.98559
H          7.78348       -1.27783       -0.79285
