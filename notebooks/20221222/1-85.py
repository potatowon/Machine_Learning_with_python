# 1-85 과목별 평균점수 구하기

scores = [[10,15,20],[20,25,30],[35,40,45],[40,45,50]]
n_student = len(scores)
n_class = len(scores[0])

class_score_sums = list()
class_score_means = list()

for _ in range(n_class):
    class_score_sums.append(0)

for student_scores in scores:
    for class_idx in range(n_class):
        class_score_sums[class_idx] += student_scores[class_idx]
print("sum of classes' scsres : {}".format(class_score_sums))

for class_idx in range(n_class):
    class_score_means.append(class_score_sums[class_idx]/n_student)
print("mean of classes' scores: {}".format(class_score_means))
