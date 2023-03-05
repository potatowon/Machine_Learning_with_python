# 1-26

scores = [10, 20, 30]
n_student = len(scores)

mean = ( scores[0] + scores[1] + scores[2])/n_student
sqare_of_mean = mean**2
mean_of_squre = (scores[0]**2 + scores[1]**2 + scores[2]**2)/n_student

variance = mean_of_squre - sqare_of_mean
std = variance**0.5

print(f'score mean: {mean}')
print(f'score standard deviation: {std}')

##
print('-----')

scores = [10, 20, 30]
n_student = len(scores)

mean = (scores[0]+ scores[1]+scores[2])/n_student
sqare_of_mean = mean**2
mean_of_squre = (scores[0]**2+scores[1]**2+scores[2]**2)/n_student

variance = mean_of_squre - sqare_of_mean
std = variance**0.5

print(f'score mean: {mean}')
print(f'score standard deviation: {std}')
print('===============')


# 1-27
print('1-27')
scores = [10, 20 , 30]
n_student = len(scores)
mean = sum(scores)/len(scores)
''' EXERCISE.0 -26 분산과 표준편차(2)'''
sqare_of_mean = mean**2
mean_of_squre = (scores[0]**2+scores[1]**2+scores[2]**2)/n_student

variance = mean_of_squre - sqare_of_mean
std = variance**0.5

print(f'score mean: {mean}')
print(f'score standard deviation: {std}')

scores[0] = (scores[0]-mean)/std
scores[1] = (scores[1] -mean)/std
scores[2] = (scores[2] - mean)/std

mean = sum(scores)/len(scores)
sqare_of_mean = mean**2
mean_of_squre = (scores[0]**2+scores[1]**2+scores[2]**2)/n_student

variance = mean_of_squre - sqare_of_mean
std = variance**0.5

print(f'score mean: {mean}')
print(f'score standard deviation: {std}')

# 아다마르 프로덕트

import numpy as np

a = np.random.randint(0, 10,(3,))
b = np.random.randint(0, 10,(3,))
print(a)
print(b)
print(a*b)
# 1-28

print('1-28')
# method.1
print('method.1')
v1, v2 = [1,2,3], [4,5,6]
v3= [v1[0]*v2[0],v1[1]*v2[1],v1[2]*v2[2]]
print(v3)

# method.2
print('method.2')
v1, v2 = [1,2,3], [4,5,6]
v3 = [0,0,0]

v3[0] = v1[0]*v2[0]
v3[1] = v1[1]*v2[1]
v3[2] = v1[2]*v2[2]
print(v3)


print('--------------')

v1, v2= [1,2,3], [4,5,6]
v3 = [v1[0]*v2[0], v1[1]*v2[1], v1[2]*v2[2] ]
print(v3)

v1, v2 = [1,2,3],[4,5,6]
v3 = [0,0,0]

v3[0]= v1[0]*v2[0]
v3[1]= v1[1]*v2[1]
v3[2]= v1[2]*v2[2]

print(v3)


# 1-29

v1 = list()

print(v1)

v1.append(1)
print(v1)
v1.append(2)
print(v1)
v1.append(3)
print(v1)

v1 = list()
print(v1)
v1.append(1)
print(v1)
v1.append(2)
print(v1)
v1.append(3)
print(v1)

v1 = list()
print(v1)
v1.append(1)
print(v1)
v1.append(2)
print(v1)

v1.append(3)
print(v1)
