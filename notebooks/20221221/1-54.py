# 1-54
# vector norm

v1 = [1,2,3]
square_sum = 0

for dim_val in v1:
    square_sum += dim_val**2
norm = square_sum**0.5
print(f'norm of v1: {norm}')

v1 = [1,2,3]
square_sum = sum(i**2 for i in v1)
norm = square_sum**0.5
print(f'norm of v1 : {norm}')

v1 = [1,2,3]
square_sum = 0

for dim_val in v1:
    square_sum += dim_val**2
norm = square_sum**0.5
print(f'norm of v1: {norm}')