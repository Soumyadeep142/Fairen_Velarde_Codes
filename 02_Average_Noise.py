from numpy import *
from matplotlib.pyplot import *

O_tot=np.zeros(100000)
N_tot=np.zeros(100000)
no_of_confg=100
for i in range(no_of_confg):
	Time, O, N=loadtxt(f"time_N_O_data_{i+1}.txt", unpack='true')
	print(i+1)
	for j in range(len(O)):
		O_tot[j]+=O[j]
		N_tot[j]+=N[j]
O_avg=[k/no_of_confg for k in O_tot]
N_avg=[l/no_of_confg for l in N_tot]

data=column_stack((Time, O_avg,  N_avg))
savetxt(f'Avg_data.txt', data, fmt='%s')
