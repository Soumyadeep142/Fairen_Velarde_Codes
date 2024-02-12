from numpy import *
from matplotlib.pyplot import *

Time, O, N=loadtxt("Avg_data.txt", unpack='true')

O_mod=[]
N_mod=[]
Time_mod=[]

for (t,o,n) in zip(Time,O,N):
	if t>3800:
		O_mod.append(o)
		N_mod.append(n)
		Time_mod.append(t)
		
data=column_stack((Time_mod, O_mod,  N_mod))
savetxt(f'Avg_data_cut.txt', data, fmt='%s', delimiter=',')

'''
scatter(O_mod, N_mod, s=0.001)
savefig('Sample.png')
show()
'''
