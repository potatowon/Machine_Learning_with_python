# 1-94 과목별 최고점, 최우수 학생 구하기
    # 각 행당 학생의 점수

scores = [[10, 40, 20],
          [50, 20, 60],
          [70, 40, 30],
          [30, 80, 40]]

n_student = len(scores)
n_class = len(scores[0])

max_calsses = scores[0] # 최댓값 구하기 초기값
max_idx_classes = list() # 각 class 당 최댓값 빈 list

# 클래스당 최댓값 list 할당
for _ in range(n_class):
    max_idx_classes.append(0)

# 최댓값 구하기
# 그때의 인덱스 값 구하기
for student_idx in range(n_student):
    student_scores = scores[student_idx] # 학생별 점수

    for class_idx in range(n_class):
        score = student_scores[class_idx] # 학생의 0,1,2 클래스의 점수
        if score > max_calsses[class_idx]:
            max_calsses[class_idx] = score
            max_idx_classes[class_idx]  = student_idx
print("Max score : {}".format(max_calsses))
print("Max score indices : {}".format(max_idx_classes))


####

scores = [[10, 40, 20],
          [50, 20, 60],
          [70, 40, 30],
          [30, 80, 40]]

n_student = len(scores)
n_class = len(scores[0])

# max 함수 초기화
max_classes = scores[0]
max_idx_classes = list()

for _ in range(n_class):
    max_idx_classes.append(0)

# 최댓값 구하기
for student_idx in range(n_student):
    student_scores = scores[student_idx]
    for class_idx in range(n_class):
        score = student_scores[class_idx]
        if score > max_classes[class_idx]:
            max_classes[class_idx] = score
            max_idx_classes[class_idx] = student_idx

print(f'Max score : {max_classes}')
print(f'max score indices : {max_idx_classes}')


#
scores = [[10, 40, 20],
          [50, 20, 60],
          [70, 40, 30],
          [30, 80, 40]]

n_student = len(scores)
n_class = len(scores[0])

max_classes = scores[0]
max_idx_classes = list()

for _ in range(n_class):
    max_idx_classes.append(0)

for student_idx in range(n_student):
    student_scores = scores[student_idx]
    for class_idx in range(n_class):
        score = student_scores[class_idx]
        if score > max_classes[class_idx]:
            max_classes[class_idx] = score
            max_idx_classes[class_idx] = student_idx

print(max_classes)
print(max_idx_classes)
