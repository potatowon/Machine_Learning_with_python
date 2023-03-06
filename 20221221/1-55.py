# 1-55
# unit vector

v1 = [1,2,3]

# norm

square_sum = 0

for dim_val in v1:
    square_sum += dim_val**2

norm = square_sum**0.5
print('norm of v1: ', norm)

# unit vector

for dim_idx in range(len(v1)):
    v1[dim_idx] /= norm
square_sum = 0
for dim_val in v1:
    square_sum += dim_val**2
norm = square_sum**0.5

print(f'norm of v1(unit vector): {norm}')

## 2
print('2')

v1 =[1,2,3]

square_sum = 0

for dim_val in v1:
    square_sum += dim_val**2
norm = square_sum**0.5
print(f'norm of v1: {norm}')

for dim_idx in range(len(v1)):
    v1[dim_idx] /= norm
square_sum = 0
for dim_val in v1:
    square_sum += dim_val**2
norm = square_sum**0.5
print(f'norm of v1 unitvector: {norm}')

print('3')

v1 =[1,2,3]

square_sum = 0
for dim_val in v1:
    square_sum += dim_val**2

norm = square_sum**0.5

for dim_idx in range(len(v1)):
    v1[dim_idx] /= norm
square_sum = 0
for dim_val in v1:
    square_sum += dim_val**2
norm = square_sum**0.5

print(f'norm of v1(unit vector): {norm}')