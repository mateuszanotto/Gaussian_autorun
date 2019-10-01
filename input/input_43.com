%nprocs=8 
%mem=16GB 
%chk=/home/mateus/github/db_singletoxygen/chk/molecule_43.chk 
#opt freq blyp/6-31g(d,p) 

molecule_43 CN(C)c1cc2c(cc1)nc1-c(cc(=[N+](C)C)cc1)s2.[Cl-]	


0 1
C          0.84365        0.34314        0.20415
N          2.29015        0.34978        0.25869
C          3.03436        0.98785       -0.83921
C          2.99264       -0.62224        0.95083
C          4.19076       -0.19980        1.46498
C          5.00897       -1.02819        2.19505
C          4.70504       -2.36268        2.44724
C          3.51567       -2.83590        1.90898
C          2.65680       -1.96152        1.19388
N          5.52342       -3.21070        3.22961
C          6.59327       -2.72465        3.76505
C          7.43420       -3.61302        4.60552
C          8.55411       -3.18762        5.19863
C          9.05713       -1.78209        5.07060
N         10.13227       -1.31173        5.61454
C         10.61503        0.11688        5.46315
C         11.02376       -2.14293        6.46248
C          8.22316       -0.91738        4.24821
C          7.12596       -1.34071        3.66131
S          6.38757       -0.13767        2.74190
Cl         1.48106       -2.26957       -2.30165
H          0.48228        1.05982       -0.54095
H          0.46018        0.67954        1.17409
H          0.39251       -0.62632       -0.00650
H          2.38420        1.53879       -1.52277
H          3.62012        0.26806       -1.42481
H          3.74241        1.73097       -0.44377
H          4.48204        0.83599        1.31827
H          3.24620       -3.88402        2.02509
H          1.75357       -2.38965        0.76792
H          7.09056       -4.63924        4.71680
H          9.08845       -3.92235        5.78406
H          9.97232        0.74028        4.84362
H         11.59644        0.09353        4.98758
H         10.64372        0.57022        6.45489
H         10.65887       -3.16184        6.55667
H         11.04979       -1.69085        7.45388
H         12.00332       -2.16770        5.98528
H          8.47724        0.12059        4.07139
