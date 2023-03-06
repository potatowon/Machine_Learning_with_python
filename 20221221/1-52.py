# Standardization

math_scores, english_scores = [50,60,70],[30,40,50]
n_student = len(math_scores)

# 분산과 표준 편차

math_sum, math_square_sum = 0,0
english_sum, english_square_sum = 0,0

for student_idx in range(n_student):
    math_sum += math_scores[student_idx]
    math_square_sum += math_scores[student_idx]**2

    english_sum += english_scores[student_idx]
    english_square_sum += english_scores[student_idx]**2

math_mean = math_sum/n_student
english_mean = english_sum/n_student

math_variance = math_square_sum/n_student - math_mean**2
english_variance = english_square_sum/n_student - english_mean**2

math_std = math_variance**0.5
english_std = english_variance**0.5

# Standardization

for student_idx in range(n_student):
    math_scores[student_idx] = (math_scores[student_idx]-math_mean)/math_std
    english_scores[student_idx] = (english_scores[student_idx] - english_mean)/english_std
print(f'Math scores after standardization: {math_scores}')
print(f'English scores after standardization: {english_scores} ')
    # 분산과 평균
math_sum, math_square_sum = 0,0
english_sum, english_square_sum = 0,0
for student_idx in range(n_student):
    math_sum += math_scores[student_idx]
    math_square_sum += math_scores[student_idx]**2

    english_sum += english_scores[student_idx]
    english_square_sum += english_scores[student_idx]**2

math_mean = math_sum/n_student
english_mean = english_sum/n_student

math_variance = (math_square_sum/n_student) - math_mean**2
english_variance = (english_square_sum/n_student) - english_mean**2

math_std = math_variance**0.5
english_std = english_variance**0.5

print(f'mean/ std of math : {math_mean},{math_std}')
print(f'mean/ std of english: {english_mean},{english_std}')

'''-------------------------------------------------------------------------------------------'''
# 2
print('--------------------------------------------------------')
math_scores, english_scores = [50,60,70],[30,40,50]

math_sum = sum(math_scores)
math_square_sum = sum([i**2 for i in math_scores])

english_sum = sum(english_scores)
english_square_sum =sum([j**2 for j in english_scores])

math_mean = math_sum/len(math_scores)
english_mean = english_sum/len(english_scores)

math_std = (math_square_sum/n_student - math_mean**2)**0.5
english_std =(english_square_sum/n_student - english_mean**2)**0.5

# Standardization

math_scores = [(i-math_mean)/math_std for i in math_scores]
english_scores = [(j-english_mean)/english_std for j in english_scores]

math_sum = sum(math_scores)
math_square_sum = sum([i**2 for i in math_scores])

english_sum = sum(english_scores)
english_square_sum =sum([j**2 for j in english_scores])

math_mean = math_sum/len(math_scores)
english_mean = english_sum/len(english_scores)

math_std = (math_square_sum/n_student - math_mean**2)**0.5
english_std =(english_square_sum/n_student - english_mean**2)**0.5

print(f'Math scores after standardization: {math_scores}')
print(f'English scores after standardization: {english_scores}')
print(f'mean/std of math : {math_mean},{math_std}')
print(f'mean/std of english {english_mean},{english_std}')
'''-------------------------------------------------------------------------------------------'''
print('--------------------------------------------------------')
math_scores, english_scores = [50,60,70],[30,40,50]

math_sum = sum(math_scores)
math_square_sum = sum([i**2 for i in math_scores])

english_sum = sum(english_scores)
english_square_sum =sum([j**2 for j in english_scores])

math_mean = math_sum/len(math_scores)
english_mean = english_sum/len(english_scores)

math_std = (math_square_sum/n_student - math_mean**2)**0.5
english_std =(english_square_sum/n_student - english_mean**2)**0.5

# Standardization

math_scores = [(i-math_mean)/math_std for i in math_scores]
english_scores = [(j-english_mean)/english_std for j in english_scores]

math_sum = sum(math_scores)
math_square_sum = sum([i**2 for i in math_scores])

english_sum = sum(english_scores)
english_square_sum =sum([j**2 for j in english_scores])

math_mean = math_sum/len(math_scores)
english_mean = english_sum/len(english_scores)

math_std = (math_square_sum/n_student - math_mean**2)**0.5
english_std =(english_square_sum/n_student - english_mean**2)**0.5

print(f'Math scores after standardization: {math_scores}')
print(f'English scores after standardization: {english_scores}')
print(f'mean/std of math : {math_mean},{math_std}')
print(f'mean/std of english {english_mean},{english_std}')