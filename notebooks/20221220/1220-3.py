# 1-30
print('1-30')

v1, v2=[1,2,3], [4,5,6]

v3 = list()
v3.append(v1[0] * v2[0])
v3.append(v1[1] * v2[1])
v3.append(v1[2] * v2[2])
print(v3)

# 1-30

print('-------')

v1, v2= [1,2,3],[4,5,6]
v3 = list()
v3.append(v1[0]*v2[0])
v3.append(v1[1]*v2[1])
v3.append(v1[2]*v2[2])
print(v3)

# 1-31
print('1-31')
v1 =[1,2,3]

norm = (v1[0]**2 + v1[1]**2 + v1[2]**2 )**0.5
print(norm)

norm = 0
norm += v1[0]**2
norm += v1[1]**2
norm += v1[2]**2
norm **= 0.5

print(norm)

print('--------')

# 1-32
v1 = [1,2,3]

norm = (v1[0]**2 + v1[1]**2+v1[2]**2)**0.5
v1 = [v1[0]/norm, v1[1]/norm, v1[2]/norm]
norm = (v1[0]**2 + v1[1]**2+v1[2]**2)**0.5
print(norm)

# 1-33 Dot product

v1 = [1,2,3]
v2= [3,4,5]
# method.1
dot_prod = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
print(dot_prod)
# method.2

dot_prod = 0
dot_prod += v1[0]*v2[0]
dot_prod += v1[1]*v2[1]
dot_prod += v1[2]*v2[2]

print(dot_prod)


# 1-34
print('-----------')
print('1-34')
v1, v2 = [1,2,3], [3,4,5]
e_distance = 0

e_distance += (v1[0]-v2[0])**2
e_distance += (v1[1]-v2[1])**2
e_distance += (v1[2]-v2[2])**2
print(e_distance**0.5)

print('--------')

v1 = [1,2,3]
v2 = [3,4,5]

e_distance = 0
e_distance += (v1[0]-v2[0])**2
e_distance += (v1[1]-v2[1])**2
e_distance += (v1[2]-v2[2])**2
print(e_distance**0.5)

# 1-35
print('-------------')
predictions = [10, 20 , 30]
label = [10, 25, 40]
n_data = len(label)

mse = 0
mse += (predictions[0] - label[0])**2
mse += (predictions[1] - label[1])**2
mse += (predictions[2] - label[2])**2
mse /= n_data
print(mse)


print('------')

predictions = [10, 20, 30]
label = [10, 25, 40]
n_data =len(label)
mse = 0
mse += (predictions[0] - label[0])**2
mse += (predictions[1] - label[1])**2
mse += (predictions[2] - label[2])**2

mse /= n_data

print(mse)




