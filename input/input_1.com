%nprocs = 8 
%mem = 16GB 
%chk=molecule_1.chk 
# opt freq b3lyp/6-31g(d,p) 

input 1

0 1
C          0.96441        0.07719       -0.04374
C          2.48429        0.08477       -0.05506
C          3.02745        0.87841       -1.24144
C          4.54734        0.88599       -1.25276
H          0.59425       -0.49553        0.81239
H          0.56848       -0.38009       -0.95599
H          0.56848        1.09492        0.03073
H          2.84985       -0.94775       -0.09849
H          2.84985        0.51900        0.88271
H          2.66190        1.91093       -1.19801
H          2.66190        0.44418       -2.17921
H          4.94327        1.34327       -0.34050
H          4.91750        1.45871       -2.10889
H          4.94327       -0.13174       -1.32723
