import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

Time, O, N=np.loadtxt('Avg_data_cut.txt', unpack='true', delimiter=',')
# Initialize empty lists to store the 2nd and 3rd columns
column_2nd = []
column_3rd = []
# Open the text file
with open('Avg_data_cut.txt', 'r') as file:
    for _ in range(len(N)+1):
        line = file.readline()
        # Check if the line is not empty
        if line:
            # Split the line by comma
            columns = line.strip().split(',')
            # Check if the line has at least 3 columns
            if len(columns) >= 3:
                # Append the 2nd and 3rd columns to their respective lists
                column_2nd.append(float(columns[1]))
                column_3rd.append(float(columns[2]))

x=column_2nd
y=column_3rd
data = np.column_stack((x, y))
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
scaling_factor=2.4
# Plot the scattered points
plt.scatter(x, y, alpha=1, s=0.01)

# Plot the ellipse
ellipse = Ellipse((np.mean(data[:,0]), np.mean(data[:,1])), scaling_factor*2*std_dev_x, scaling_factor*2 * std_dev_y, angle=np.degrees(theta), edgecolor='r', fill=False, lw=2)
plt.gca().add_patch(ellipse)

# Set plot labels and title
plt.xlabel('Oxygen')
plt.ylabel('Nutrient')
plt.show()
semi_major = scaling_factor * 2 * std_dev_x
semi_minor= scaling_factor * 2 * std_dev_y
area=np.pi*semi_major*semi_minor
print("Semi-major axis", semi_major, "Semi-minor axis", semi_minor)
print("The area of the ellipse is:",area)
