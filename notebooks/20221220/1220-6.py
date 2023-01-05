## 1- 46

scores = [10,20,30]
score_sum =0
#method.1

for i in scores:
    score_sum += i
score_mean = score_sum / len(scores)
print(score_mean)
scores_ms = list()

for score in scores:
    scores_ms.append(score - score_mean)
print(scores_ms)

# method. 2
scores = [10,20,30]
score_sum =0
for i in scores:
    score_sum += i
score_mean = score_sum / len(scores)

for score_idx in range(len(scores)):
    scores[score_idx] -= score_mean
print(scores)


# 두 과목의 평균을 구하기

math_score = [40, 60 , 80]
eglish_score = [30, 40, 50]

n_class = 2
n_student = len(math_score)

score_sums = list()
score_means = list()

for _ in range(n_class):
    score_sums.append(0) # 자리 값의 세팅


for student_idx in range(n_student):
    score_sums[0] += math_score[student_idx]
    score_sums[1] += eglish_score[student_idx]

print(f'sum fo scores : {score_sums}')

for class_idx in range(n_class):
    class_mean = score_sums[class_idx]/n_student
    score_means.append(class_mean)

print(f'mean of scores: {score_means}')