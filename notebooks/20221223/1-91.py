# 1-91 Making Unit vectior(4)

vectors = [[1, 11, 21],
           [2, 12, 22],
           [3, 13, 23],
           [4, 14, 24]]
# norm 구하기
n_vecter = len(vectors[0])
v_norm = list()

for _ in range(n_vecter):
    v_norm.append(0)

for dim_data in vectors:
    for dim_idx in range(n_vecter):
        v_norm[dim_idx] += dim_data[dim_idx]**2

for vec_idx in range(n_vecter):
    v_norm[vec_idx] **= 0.5
print(v_norm)
# nuit vector
n_dim = len(vectors)  # 차원 수
n_vecter = len(vectors[0])

for dim_idx in range(n_dim):
    for vec_idx in range(n_vecter):
        vectors[dim_idx][vec_idx] /= v_norm[vec_idx] # n 차원의 m 번 벡터

print(vectors)
# norm 구하기
n_vecter = len(vectors[0])
v_norm = list()
for _ in range(n_vecter):
    v_norm.append(0)

for dim_data in vectors:
    for vec_idx in range(n_vecter):
        v_norm[vec_idx] += dim_data[vec_idx]**2

for vec_idx in range(n_vecter):
    v_norm[vec_idx] **= 0.5

print(v_norm)

###########
vectors = [[1, 11, 21],
           [2, 12, 22],
           [3, 13, 23],
           [4, 14, 24]]

# 1. norm vector 구하기
n_vecter = len(vectors[0])
v_norm = list()

for _ in range(n_vecter):
    v_norm.append(0)

for dim_data in vectors:
    for dim_idx in range(n_vecter):
        v_norm[dim_idx] += dim_data[dim_idx]**2

for vec_idx in range(n_vecter):
    v_norm[vec_idx] **= 0.5

print(v_norm)

# 2. unit vector 구하기 ( vector / norm )

for dim_idx in range(len(vectors)):
    for vec_idx in range(n_vecter):
        vectors[dim_idx][vec_idx] /= v_norm[vec_idx]

print(vectors)

# 3. unit vector 의 norm 구하기

v_norm = list()

for _ in range(n_vecter):
    v_norm.append(0)
for dim_data in vectors:
    for vec_idx in range(n_vecter):
        v_norm[vec_idx] += dim_data[vec_idx]**2
for vec_idx in range(n_vecter):
    v_norm[vec_idx] **= 0.5

print(v_norm)

print('화장실 갔다오고 싶당')

