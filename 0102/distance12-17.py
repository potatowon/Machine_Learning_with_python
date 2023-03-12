
import numpy as np

d17 = np.array([5.25, 9.50])
d12 = np.array([5.00, 2.50])

# Euclidean distance
euclidean_d = sum((d12 - d17) ** 2) ** 0.5
print(f'Euclidean distance : {euclidean_d}')

# Manhattan distance
manhattan_d = sum(abs(d12 - d17))
print(f'Manhattan distance { manhattan_d}')
