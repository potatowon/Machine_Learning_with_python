# 1-48
# Mean Subtraction (4)

math_scores = [40,60,80]
english_scores = [30,40,50]
n_student = len(math_scores)

math_mean = sum(math_scores)/len(math_scores)
english_mean = sum(english_scores)/len(english_scores)

for student_idx in range(n_student):
    math_scores[student_idx] -= math_mean
    english_scores[student_idx] -= english_mean

print(f'Math scores after mean subtraction: {math_scores}')
print(f'English scores after mean subtraction: {english_scores}')
'''--------------------------------------------------------------------------'''
math_scores =[40, 60, 80]
english_scores = [30,40,50]
n_student = len(english_scores)

math_mean = sum(math_scores)/len(math_scores)
english_mean = sum(english_scores)/len(english_scores)

for student_idx in range(n_student):
    math_scores[student_idx] -= math_mean
    english_scores[student_idx] -= english_mean

print(f'math scores after mean subtraction: {math_scores}')
print(f'english scores after mean subtraction: {english_scores}')
'''--------------------------------------------------------------------------'''
math_scores = [40, 60, 80]
english_scores = [30, 40, 50]
n_student = len(math_scores)

math_mean = sum(math_scores)/len(math_scores)
english_mean =sum(english_scores)/len(english_scores)

for student_idx in range(n_student):
    math_scores[student_idx] -= math_mean
    english_scores[student_idx] -= english_mean

print(f'math scores after mean subtraction: {math_scores}')
print(f'English scores after mean subtraction: {english_scores}')
'''--------------------------------------------------------------------------'''

# 1-49
print('1')
scores = [10,20,30]
n_student =len(scores)
score_sum, score_square_sum = 0, 0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum/n_student
square_of_mean = score_square_sum/n_student

variance = square_of_mean - mean**2
std = variance**0.5

print(f'variance : {variance}')
print(f'standard deviation : {std}')
'''---------------------------------------'''
print('2')

scores = [10,20,30]
n_student = len(scores)
score_sum, score_square_sum = 0, 0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum / len(scores)
square_of_mean = score_square_sum/ n_student

variance = square_of_mean - mean**2
std = variance**0.5

print(f'variance: {variance}')
print(f'standard deviation: {std}')

print('3')

scores = [10,20,30]
n_student = len(scores)
score_sum, score_square_sum = 0,0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum / n_student
square_of_mean = score_square_sum / n_student

variance = square_of_mean - mean**2
std = variance**0.5

print(f'variance: {variance}')
print(f'standard deviation: {std}')

'''--------------------------------------------------------------------------'''
# 1-50
# Standardiztion(3)

scores = [10, 20, 30]
score_sum, score_square_sum = 0,0


for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum/len(scores)
square_of_mean = score_square_sum / len(scores)

variance = square_of_mean - mean**2
std = variance**0.5

for student_idx in range(len(scores)):
    scores[student_idx] = (scores[student_idx]-mean)/std
print(scores)


mean = sum(scores)/len(scores)
square_of_score = [i**2 for i in scores]
square_of_mean = sum(square_of_score)/len(scores)

variance = square_of_mean - mean**2
std = variance**0.5
print(f'mean: {mean}')
print(f'standard deviation: {std}')
'''---------------------------------------------------------------------------'''

print('2')

scores = [10,20,30]

# 평균과 분산
n_student = len(scores)
score_sum, square_of_score = 0,0

for score in scores:
    score_sum += score
    square_of_score += score**2

mean = score_sum / n_student
square_of_mean = square_of_score / n_student

variance = square_of_mean - mean**2
std = variance**0.5

# standardization

for student_idx in range(len(scores)):
    scores[student_idx] = (scores[student_idx] - mean)/std

# 평균 분산

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum/n_student
square_of_mean = score_square_sum/n_student

variance = square_of_mean -mean**2
std = variance**0.5

print(scores)
print(f'variance : {variance}')
print(f'standard deviation: {std}')
'''---------------------------------------------------------------------------'''

print('3')

scores = [10,20,30]

# 평균과 분산

n_student = len(scores)
score_sum, score_square_sum = 0,0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum / n_student
square_of_mean = score_square_sum / n_student

variance = square_of_mean - mean**2
std = variance**0.5

# 정규화

for student_idx in range(n_student):
    scores[student_idx] = (scores[student_idx] - mean)/std

# 평균과 분산
for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum/n_student
square_of_mean = score_square_sum/n_student

variance = square_of_mean - mean**2
std = variance**0.5

print(scores)
print(f'variance: {variance}')
print(f'Standard deviation: {std}')