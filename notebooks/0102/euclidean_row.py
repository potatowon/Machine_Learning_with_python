'''
test_instance 와 instances 사이의 euclidean distance
'''
import numpy as np

instances = np.array([ [5, 2.5, 3],
                       [2.75, 7.50, 4],
                       [9.10, 4.5, 4],
                       [8.9, 2.3, 6]])
test_instance = instances[0]
distances = []

for instance in instances:
    distance = np.sqrt(np.sum((instance - test_instance)**2))
    distances.append(distance)
print(distances)
