# 분산과 표준편차
print('1')
math_score, english_score = [50,60,70], [30,40,50]
n_student = len(math_score)
# 합 초기화
math_sum, english_sum = 0,0
math_square_sum, english_square_sum = 0,0

# 평균, 분산

for student_idx in range(n_student):
    math_sum += math_score[student_idx]
    math_square_sum += math_score[student_idx]**2

    english_sum += english_score[student_idx]
    english_square_sum += english_score[student_idx]**2

math_mean = math_sum / n_student
english_mean = english_sum /n_student

math_variance = (math_square_sum/n_student) - math_mean**2
english_variance = (english_square_sum/n_student) - english_mean**2

math_std = math_variance**0.5
english_std = english_variance**0.5

print(f'mean/std of Math: {math_mean, math_std}')
print(f'mean/std of English: {english_mean, english_std}')


print('2')

math_score, english_score = [50,60,70], [30,40,50]
n_student = len(math_score)

# 합 초기화

math_sum, math_square_sum = 0,0
english_sum, english_square_sum = 0,0

# 평균 과 분산

for student_idx in range(n_student):
    math_sum += math_score[student_idx]
    math_square_sum += math_score[student_idx]**2

    english_sum += english_score[student_idx]
    english_square_sum += english_score[student_idx]**2

math_mean = math_sum/n_student
english_mean = english_sum/n_student

math_variance = math_square_sum/n_student - math_mean**2
english_variance = english_square_sum/n_student - english_mean**2

math_std = math_variance**0.5
english_std = english_variance**0.5

print(f'mean/ std of Math: {math_mean},{math_std}')
print(f'mean/ std of English: {english_mean}, {english_std}')

print('3')

math_score, english_score = [50,60,70],[30,40,50]
n_student = len(math_score)
# 합 초기화

math_sum, math_square_sum = 0,0
english_sum, english_square_sum = 0,0

# 평균과 분산

for student_idx in range(n_student):
    math_sum += math_score[student_idx]
    math_square_sum += math_score[student_idx]**2

    english_sum += english_score[student_idx]
    english_square_sum += english_score[student_idx]**2

math_mean = math_sum/n_student
english_mean = english_sum/n_student

math_variance = math_square_sum/n_student - math_mean**2
english_variance = english_square_sum/n_student - english_mean**2

math_std = math_variance**0.5
english_std = english_variance**0.5

print(f'mean/ std of Math: {math_mean},{math_std}')
print(f'mean/ std of English: {english_mean}, {english_std}')