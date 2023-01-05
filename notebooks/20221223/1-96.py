# 1-96 Accuracy 구하기
# One-hot- encoding 된 상태에서의 accuracy를 구해 봅시다
predictions =[[1, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1]]

labels = [0,1,2,1,0,3]

n_class = 0

for label in labels:
    if label > n_class:
        n_class = label
n_class += 1
one_hot_mat = list()

for label in labels:
    one_hot_vec = list()
    for _ in range(n_class):
        one_hot_vec.append(0)
    one_hot_vec[label] = 1
    one_hot_mat.append(one_hot_vec)
print(one_hot_mat)

n_pred = len(predictions)
n_class = len(predictions[0])

accuracy = 0
for pred_idx in range(n_pred):
    prediction = predictions[pred_idx]
    label = one_hot_mat[pred_idx]

    correct_cnt = 0

    for class_idx in range(n_class):
        if prediction[class_idx] == label[class_idx]:
            correct_cnt += 1
    if correct_cnt == n_class:
        accuracy += 1

accuracy /= n_pred
print(f'accuracy: {accuracy}')