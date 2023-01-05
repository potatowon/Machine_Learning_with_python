# for 문 접근하기

scores = [10, 20 ,30]

#method.1
for score in scores:
    print(score)

#method.2

for score_idx in range(len(scores)):
    print(scores[score_idx])

# 연습

scores =[20, 30 ,40]
for score in scores:
    print(score)

for score_idx in range(len(scores)):
    print(scores[score_idx])

scores = [10, 20, 30 ]
for score in scores:
    print(score)
for score_idx in range(len(scores)):
    print(scores[score_idx])


# list 의 원소 수정하기

scores = [10, 20, 30, 40, 50]

for score_idx in range(len(scores)):
    scores[score_idx] += 10
print(scores)

scores = [1,2,3,4,5,6]

for score_idx in range(len(scores)):
    scores[score_idx] += 10
print(scores)


scores = [10, 20, 30, 40 , 50]

for score_idx in range(len(scores)):
    scores[score_idx] += 10
print(scores)


# 두개의 List 접근하기

lst1 = [10, 20, 30]
lst2 = [100, 200, 300]

for idx in range(len(lst1)):
    print(lst1[idx], lst2[idx])


lst1 = [10,20,30]
lst2 =[100,200, 300]

for idx in range(len(lst1)):
    print(lst1[idx],lst2[idx])

# 수학 점수들의 평균 구하기

scores = [10, 20, 30]

# method.1

score_sum = 0
n_student = 0
for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum / n_student
print(f'score mean: {score_mean}')

#method.2

score_sum = 0

for score_idx in range(len(scores)):
    score_sum += scores[score_idx]
score_mean = score_sum/ len(scores)
print(f'score mean: {score_mean}')

#

scores = [10,20,30]
score_sum = 0
n_student = 0

for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum / n_student
print(f'score mean: {score_mean}')

for score_idx in range(len(scores)):
    score_sum += scores[score_idx]
score_mean = score_sum / len(scores)
print(f'score mean: {score_mean}')

scores = [10,20,30]
score_sum = 0
n_student = 0
for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum/n_student
print(f'score mean: {score_mean}')

for score_idx in range(len(scores)):
    score_sum += scores[score_idx]
score_mean = score_sum /len(scores)
print(f'score mean: {score_mean}')

## 1- 46

scores = [10,20,30]

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
for i in scores:
    score_sum += i
score_mean = score_sum / len(scores)

for score_idx in range(len(scores)):
    scores[score_idx] -= score_mean
print(scores)