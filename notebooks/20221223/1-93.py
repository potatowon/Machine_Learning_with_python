# 1-93 Euclidean Distance(4)

vectors = [[1, 11],
           [2, 12],
           [3, 13],
           [4, 14] ]

e_distance = 0

for dim_data in vectors:
    diff = dim_data[0] - dim_data[1]
    diff_square = diff**2
    e_distance += diff_square

e_distance **= 0.5
print('Euvlidean distance : {}'.format(e_distance))


######
e_distance = 0

diff_square = [(dim_data[0]-dim_data[1])**2 for dim_data in vectors]
e_distance = sum(diff_square)**0.5

print(e_distance)

# 두점 사이의 거리제곱의 합

e_distance = 0
for dim_data in vectors:
    diff = dim_data[0] - dim_data[1]
    diff_square = diff**2
    e_distance += diff_square
e_distance **= 0.5

print(e_distance)