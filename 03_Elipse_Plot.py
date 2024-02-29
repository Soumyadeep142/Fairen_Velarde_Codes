import numpy as np
from matplotlib.pyplot import *

for st in range(19):
	try:
		no, fixed_pt=np.loadtxt(f'Elipse_Analysis/analysed_data_{st+1}.txt', unpack='true')

		semi_major_point=[]
		semi_minor_point=[]
		area_point=[]

		for (i,j) in zip(no, fixed_pt):
			#print(i)
			Time, N, O=np.loadtxt(f'F_{st+1}/t_{int(i)}.txt', unpack='true')
			Time_New=[]
			N_New=[]
			O_New=[]
			for (k,l,m) in zip(Time, N, O):
				if k>=j:
					Time_New.append(k)
					N_New.append(l)
					O_New.append(m)

			# Combine the Oxygen and Nutrient data into a single array
			data = np.column_stack((O_New, N_New))

			# Calculate the covariance matrix
			cov_matrix = np.cov(data, rowvar=False)

			# Find the eigenvalues and eigenvectors of the covariance matrix
			eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

			# Sort eigenvalues and eigenvectors
			sorted_indices = np.argsort(eigenvalues)[::-1]
			eigenvalues = eigenvalues[sorted_indices]
			eigenvectors = eigenvectors[:, sorted_indices]

			# Calculate the angle of rotation for the ellipse
			theta = np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0])

			# Calculate the semi-axes lengths (standard deviations along each principal component)
			std_dev_x = np.sqrt(eigenvalues[0])
			std_dev_y = np.sqrt(eigenvalues[1])

			# Automatically determine the scaling factor based on a confidence interval or multiplier
			confidence_interval = 0.99  # Adjust as needed
			scaling_factor = np.sqrt(-2 * np.log(1 - confidence_interval))

			semi_major = scaling_factor * 2 * std_dev_x
			semi_minor = scaling_factor * 2 * std_dev_y
			area = np.pi * semi_major * semi_minor
			
			semi_major_point.append(semi_major)
			semi_minor_point.append(semi_minor)
			area_point.append(area)

		data=np.column_stack((no, fixed_pt, semi_major_point, semi_minor_point, area_point))
		np.savetxt(f'Elipse_Analysis/elipse_analysis_{st+1}.txt', data, fmt='%s')
	except:
		print(st+1)
