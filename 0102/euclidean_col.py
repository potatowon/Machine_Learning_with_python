'''
col vector euclidean col
'''
import numpy as np

instances = np.array([ [5, 2.5, 3],
                       [2.75, 7.50, 4],
                       [9.10, 4.5, 4],
                       [8.9, 2.3, 6]])
print(instances)
test_instance = instances[:, 0]

n_cols = instances.shape[1]  # column의 갯수
# instances.shape 4 by 3 (4,3) tuple
distances = []

for col_idx in range(n_cols):
    instance = instances[:, col_idx] # col vector 뽑아내기
    distance = np.sqrt(np.sum((instance- test_instance)**2))
    distances.append(distance)
print(distances)
