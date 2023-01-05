# 1-95 One-hot Encoding

labels = [1,2,3,1,0,3] # 4가지 class -> 0,1,2,3 / class당 각 인덱스 할당
# 0 class -> [1, 0, 0, 0] vec
# 1 class -> [0, 1, 0, 0] vec
# 2 class -> [0, 0, 1, 0] vec
# 3 class -> [0, 0, 0, 1] vec

# I love 목적 > 목적에 들어가는 vec을 확률적으로 학습하여 알려줌
# ex) AI chat bot

n_label = len(labels)
n_class = 0

# 클래스의 개수 구하기
for label in labels:
    if label > n_class:
        n_class = label
n_class += 1 # n_class = 4
one_hot_mat = list()
for label in labels:
    one_hot_vec = list()
    for _ in range(n_class):
        one_hot_vec.append(0)
    one_hot_vec[label] = 1

    one_hot_mat.append(one_hot_vec)

print(one_hot_mat)


####

labels = [1,2,3,1,0,3]

n_class = 0
# class의 갯수 구하기
for label in labels:
    if label > n_class:
        n_class = label
print(n_class)
n_class += 1
# one hot mat 구하기

one_hot_mat = list()
for label in labels:
    one_hot_vec =list()
    for _ in range(n_class):
        one_hot_vec.append(0)
    one_hot_vec[label] = 1

    one_hot_mat.append(one_hot_vec)
print(one_hot_mat)



# 1. class 의 갯수 구하기
n_class = 0

for label in labels:
    if label > n_class:
        n_class = label
n_class += 1

# 2. one hot matrix 구하기

one_hot_mat = list()

for label in labels:
    one_hot_vec = list()
    for _ in range(n_class):
        one_hot_vec.append(0)
    one_hot_vec[label] = 1
    one_hot_mat.append(one_hot_vec)
print(one_hot_mat)

