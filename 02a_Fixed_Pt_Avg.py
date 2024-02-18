from numpy import *
from matplotlib.pyplot import *

total_number=[]
avg_time=[]
i_range=[]
noise_range=[]
noise=0.5
for i in range(7,30):
	no, time=loadtxt(f'analysed_data_{i+1}.txt', unpack='true')
	total_number.append(len(no))
	avg_time.append(mean(time))
	i_range.append(i+1)
	noise_range.append(noise)
	noise+=0.05
data1=column_stack((noise_range, total_number, avg_time))
savetxt(f'Fixed_pt_analysis.txt', data1, fmt='%s')

log_avg_time=[log(i) for i in avg_time]
data1=column_stack((noise_range, total_number, log_avg_time))
savetxt(f'Log_Fixed_pt_analysis.txt', data1, fmt='%s')
