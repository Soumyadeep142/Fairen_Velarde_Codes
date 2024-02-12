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

# Iterate over different confidence intervals
confidence_intervals = [0.68, 0.95, 0.99]  # Add more if needed

plt.scatter(O, N, alpha=1, s=0.01)

for confidence_interval in confidence_intervals:
    # Calculate the scaling factor for each confidence interval
    scaling_factor = np.sqrt(-2 * np.log(1 - confidence_interval))

    # Calculate the angle of rotation for the ellipse
    theta = np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0])

    # Calculate the semi-axes lengths (standard deviations along each principal component)
    std_dev_x = np.sqrt(eigenvalues[0])
    std_dev_y = np.sqrt(eigenvalues[1])

    # Plot the ellipse
    ellipse = Ellipse((np.mean(data[:, 0]), np.mean(data[:, 1])),
                      scaling_factor * 2 * std_dev_x, scaling_factor * 2 * std_dev_y,
                      angle=np.degrees(theta), edgecolor='r', fill=False, lw=2)
    plt.gca().add_patch(ellipse)

    print(f"Confidence Interval: {confidence_interval:.2f}")
    print("Semi-major axis:", scaling_factor * 2 * std_dev_x)
    print("Semi-minor axis:", scaling_factor * 2 * std_dev_y)
    print()

# Set plot labels and title
plt.xlabel('Oxygen')
plt.ylabel('Nutrient')
plt.show()



