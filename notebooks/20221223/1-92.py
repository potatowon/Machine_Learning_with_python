# 1-92 Dot product(4)

vectors = [[1, 11],
           [2, 12],
           [3, 13],
           [4, 14]]

d_prod = 0
for dim_data in vectors:
    d_prod += dim_data[0]*dim_data[1]
print('dot product:', d_prod)

d_prod = 0
for dim_data in vectors:
    d_prod += dim_data[0]*dim_data[1]
print(d_prod)

d_prod = 0

for dim_data in vectors:
    d_prod += dim_data[0]*dim_data[1]

print('Dot product: {}'.format(d_prod))