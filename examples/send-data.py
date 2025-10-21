import vizlab
import numpy as np
import matplotlib.pyplot as plt

# Create datasets
positions = np.random.rand(1000, 3)
scalar = np.random.rand(1000)

# Create figure
fig, ax = plt.subplots()
x_data = np.linspace(0, 10, 100)
y_data = np.cos(x_data)
ax.plot(x_data, y_data, label='Cosine', color='blue', linestyle='--')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Cosine Plot')
ax.legend()

# Send data over to VizLab
vizlab.send([positions, scalar, fig])