# 1-84

scores = [[10,15,20],[20,25,30],[35,40,45],[40,45,50]]

n_class = len(scores[0])
student_score_means = list()

for student_score in scores:
    student_score_sum = 0
    for score in student_score:
        student_score_sum += score
    student_score_means.append(student_score_sum/n_class)

print("Mean of students' score: {0}".format(student_score_means))

##

n_class = len(scores[0])
student_score_means = list()

for student_score in scores:
    student_score_sum = 0
    for score in student_score:
        student_score_sum += score
    student_score_means.append(student_score_sum/n_class)
print(student_score_means)

##

student_score_means = list()

for score in scores:
    student_score_means.append(sum(score)/len(score))
print(student_score_means)