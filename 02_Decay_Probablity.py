from numpy import *
from matplotlib.pyplot import *
from params import *

count=0
file_name=[]
Time_Fixed=[]
for ic in range(1,no_of_confg+1,1):
	print(ic)
	Time, Oxygen, Nutrient=loadtxt(f'time_N_O_data_{ic}.txt', unpack='true')

	Peak_Oxygen_points=[]
	Peak_Oxygen_Time=[]
	Deep_Oxygen_points=[]
	Deep_Oxygen_Time=[]
	Peak_Nutrient_points=[]
	Peak_Nutrient_Time=[]
	Deep_Nutrient_points=[]
	Deep_Nutrient_Time=[]

	for i in range(1, len(Time)-1):
		if (Oxygen[i-1]<Oxygen[i]) and (Oxygen[i+1]<Oxygen[i]):
			Peak_Oxygen_points.append(Oxygen[i])
			Peak_Oxygen_Time.append(Time[i])
			
		if (Oxygen[i-1]>Oxygen[i]) and (Oxygen[i+1]>Oxygen[i]):
			Deep_Oxygen_points.append(Oxygen[i])
			Deep_Oxygen_Time.append(Time[i])
			
		if (Nutrient[i-1]<Nutrient[i]) and (Nutrient[i+1]<Nutrient[i]):
			Peak_Nutrient_points.append(Nutrient[i])
			Peak_Nutrient_Time.append(Time[i])
			
		if (Nutrient[i-1]>Nutrient[i]) and (Nutrient[i+1]>Nutrient[i]):
			Deep_Nutrient_points.append(Nutrient[i])
			Deep_Nutrient_Time.append(Time[i])
			
	ran=min([len(Peak_Oxygen_points), len(Deep_Oxygen_points), len(Peak_Nutrient_points), len(Deep_Nutrient_points)])
	Deep_Peak_Oxygen=[]
	Deep_Peak_Nutrient=[]
	New_Time=[]
	for i in range(ran):
		Deep_Peak_Oxygen.append(abs(Peak_Oxygen_points[i]-Deep_Oxygen_points[i]))
		Deep_Peak_Nutrient.append(abs(Peak_Nutrient_points[i]-Deep_Nutrient_points[i]))
		New_Time.append(i+1)

	Deep_Peak_Oxygen.pop(0)
	Deep_Peak_Nutrient.pop(0)
	New_Time.pop(0)

	#log_Oxygen=[log(i) for i in Deep_Peak_Oxygen]
	#log_Nutrient=[log(i) for i in Deep_Peak_Nutrient]
	
	for i in range(len(Deep_Peak_Oxygen)):
		if Deep_Peak_Oxygen[i]<0.5:
			count+=1
			Time_Fixed.append((Deep_Oxygen_Time[i]+Peak_Oxygen_Time[i])/2)
			file_name.append(ic)
			break
print(count)
data=column_stack((file_name, Time_Fixed))
savetxt(f'analysed_data.txt', data, fmt='%s')

