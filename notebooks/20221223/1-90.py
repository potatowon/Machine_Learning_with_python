# 1-90 Vector Norm(4)

vectors =[[1, 11, 21],
          [2, 12, 22],
          [3, 13, 23],
          [4, 14, 24]]
n_vector = len(vectors[0])

v_norms = list()
for _ in range(n_vector):
    v_norms.append(0)
print(v_norms)

for dim_data in vectors:
    for dim_idx in range(n_vector):
        v_norms[dim_idx] += dim_data[dim_idx]**2
print(v_norms)

for vec_idx in range(n_vector):
    v_norms[vec_idx] **= 0.5
print(v_norms)

#

v_norms = list()

# v_norms setting

for _ in range(n_vector):
    v_norms.append(0)
print(v_norms)

# 제곱의 합

for dim_data in vectors:
    for dim_idx in range(n_vector):
        v_norms[dim_idx] += dim_data[dim_idx]**2
print(v_norms)

# square

for vec_idx in range(n_vector):
    v_norms[vec_idx] **= 0.5

print(v_norms)

#

n_vector = len(vectors[0])

v_norms = list()

for _ in range(n_vector):
    v_norms.append(0)
print(v_norms)

for dim_data in vectors:
    for dim_idx in range(n_vector):
        v_norms[dim_idx] += dim_data[dim_idx]**2
print(v_norms)

for vec_idx in range(n_vector):
    v_norms[vec_idx] **= 0.5
print(v_norms)