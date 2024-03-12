from numpy import *
from matplotlib.pyplot import *

total_number=[]
avg_time=[]
i_range=[]
noise_range=[0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,0.35,0.4,0.45,0.5]
area_range=[]
noise_new=[]
std_time=[]
std_area=[]
for i in range(22):
	try:
		no, time=loadtxt(f'analysed_data_{i+1}.txt', unpack='true')
		area=loadtxt(f'elipse_analysis_{i+1}.txt', usecols=(4), unpack='true')
		total_number.append(len(no)/1000)
		avg_time.append(mean(time))
		i_range.append(i+1)
		area_range.append(mean(area))
		noise_new.append(noise_range[i])
		std_time.append(std(time)/sqrt(len(no)))
		std_area.append(std(area)/sqrt(len(no)))
	except:
		print(i+1)
data1=column_stack((noise_new, total_number, avg_time, area_range, std_time, std_area))
savetxt(f'Fixed_pt_analysis.txt', data1, fmt='%s')

#log_avg_time=[log(i) for i in avg_time]
#data1=column_stack((noise_range, total_number, log_avg_time))
#savetxt(f'Log_Fixed_pt_analysis.txt', data1, fmt='%s')
