import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# Load data from the file
Time, O, N = np.loadtxt('Avg_data_cut.txt', unpack=True, delimiter=',')

# Combine the Oxygen and Nutrient data into a single array
data = np.column_stack((O, N))

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
confidence_interval = 0.95  # Adjust as needed
scaling_factor = np.sqrt(-2 * np.log(1 - confidence_interval))

# Plot the scattered points
plt.scatter(O, N, alpha=1, s=0.01)

# Plot the ellipse
ellipse = Ellipse((np.mean(data[:, 0]), np.mean(data[:, 1])),
                  scaling_factor * 2 * std_dev_x, scaling_factor * 2 * std_dev_y,
                  angle=np.degrees(theta), edgecolor='r', fill=False, lw=2)
plt.gca().add_patch(ellipse)

# Set plot labels and title
plt.xlabel('Oxygen')
plt.ylabel('Nutrient')
plt.show()

semi_major = scaling_factor * 2 * std_dev_x
semi_minor = scaling_factor * 2 * std_dev_y
area = np.pi * semi_major * semi_minor

print("Semi-major axis", semi_major, "Semi-minor axis", semi_minor)
print("The area of the ellipse is:", area)
