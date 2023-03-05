# 1-21 Mean Square Error

pred1, pred2, pred3 = 10, 20, 30
y1, y2, y3 = 10, 25, 40
n_data = 3

s_error1 = (pred1 - y1)**2
s_error2 = (pred2 - y2)**2
s_error3 = (pred3 - y3)**2

mes = (s_error1+ s_error2 + s_error3 )/ n_data
print(mes)


# 1-22

score = [10, 20, 30]
print(score[0])
print(score[1])
print(score[2])

score = [10, 20, 30]
print(score[0])
print(score[1])
print(score[2])

score = [10,20,30]
print(score[0])
print(score[1])
print(score[2])

# 1-23 리스트 원소 수정하기

score = [10, 20 , 30]
print(score)

score[0] = 100
score[1] =200
print(score)
print('구분선')
score= [10, 20 , 39]
print(score)

score[0] = 100
score[2] = 300

print(score)
print('구분선')
score = [10, 20, 30]
print(score)
score[0] = 100
score[1] = 200
print(score)
print('구분선')

# 1-24
score = [10, 20, 30]
n_students = len(score)

mean = (score[0] + score[1]+ score[2])/n_students
print(f'score mean: {mean}')

print('-----')

score = [80, 90, 100]
n_students = len(score)

mean = (score[0]+ score[1] + score[2])/n_students
print(f'score mean: {mean}')
print('-----')
score = [80, 90, 100]
n_students = len(score)

mean = (score[0]+ score[1] + score[2])/n_students
print(f'score mean: {mean}')
print('-----')

# 1-25
print('1-25')

score = [10, 20, 30]
n_students = len(score)
mean = (score[0] + score[1] + score[2])/n_students
print(f'score mean: {mean}')

score[0] -= mean
score[1] -= mean
score[2] -= mean

mean = (score[0]+ score[1]+ score[2])/n_students
print(f'score mean: {mean}')

print('--------')

score = [10, 20, 30]
n_students = len(score)
mean = (score[0] + score[1] + score[2])/n_students
print(f'score mean: {mean}')

score[0] -= mean
score[1] -= mean
score[2] -= mean

mean = (score[0]+ score[1]+ score[2])/n_students
print(f'score mean: {mean}')

print('-------')

score = [10, 20, 30]
n_students = len(score)
mean = (score[0] + score[1] + score[2])/n_students
print(f'score mean: {mean}')

score[0] -= mean
score[1] -= mean
score[2] -= mean

mean = (score[0]+ score[1]+ score[2])/n_students
print(f'score mean: {mean}')


