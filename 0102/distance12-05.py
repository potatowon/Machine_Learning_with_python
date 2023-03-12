
import numpy as np

v1 = np.array([2.75, 7.5])
v2 = np.array([5.00, 2.50])

# Euclidean distance
euclidean_d = sum((v1-v2)**2)**0.5
print(f'Euclidean distance : {euclidean_d}')

# Manhattan distance
manhattan_d = sum(abs(v1-v2))
print(f'Manhattan distance { manhattan_d}')

# for 문

d5 = [2.75, 7.50]
d12 = [5.00, 2.50]
square_sum = 0

for dim_idx in range(len(d12)):
    square_sum += (d5[dim_idx] - d12[dim_idx])**2
e_d = square_sum**0.5

sub = 0
for dim_idx in range(len(d12)):
    if d5[dim_idx] > d12[dim_idx]:
        sub += d5[dim_idx] - d12[dim_idx]
    elif d5[dim_idx] < d12[dim_idx]:
        sub += d12[dim_idx] - d5[dim_idx]


print(f'Euclidean distance : {e_d}')
print(f'Mangattan distance : {sub}')

## list in list

instances = [[5.00, 2.50],
              [2.75, 7.50]]

diff = 0

for dim_idx in range(len(instances[0])):
    diff += (instances[0][dim_idx] - instances[1][dim_idx])**2
e_distance = diff **0.5
print(f"euclidean distance: {e_distance}")

abs_sum = 0

for dim_idx in range(len(instances[0])):
    diff = instances[0][dim_idx] - instances[1][dim_idx]
    if diff < 0:
        abs_sum += -diff
    if diff >0:
        abs_sum += diff
m_distance = abs_sum
print(f'manhattan distance: {m_distance}')

print(np.transpose(instances))
test_matrix = np.array(instances)
print(test_matrix.T)

