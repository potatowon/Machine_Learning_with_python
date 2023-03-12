import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([3, 4, 5])

e_distance = (v1-v2)**2
e_distance = sum(e_distance)**0.5
print(e_distance)

num1 = [1,2,3]
num2 =[4,5,6]
num1.append(num2)
print(num1)