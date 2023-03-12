# Manhattan Distance

import numpy as np

v1 = [1, 3, 5, 2, 1, 5, 2]
v2 = [2, 3, 1, 5, 2, 1, 3]

m_distance = 0

v1 = np.array(v1)
v2 = np.array(v2)

m_distance = np.abs(v1-v2)
m_distance = sum(m_distance)
print(m_distance)