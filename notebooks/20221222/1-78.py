# 1-78 Confusion Vector 구하기 클래스 별로 정확도 확인

# 이진 분류
# 모델이 예측한 값, 실제값
# 모델이 Positive/ nagative
# 실제 p/n
# -> 2x2 matrix

predictions = [0,1,0,2,1,2,0]
labels = [1,1,0,0,1,2,1]

M_class = None

for lable in labels:
    if M_class == None or lable > M_class:
        M_class = lable

M_class += 1
print(M_class)
class_cnts, correct_cnts, confusion_vec = list(), list(), list()

for _ in range(M_class):
    class_cnts.append(0)
    correct_cnts.append(0) # 값을 더해주기 위해서 0을 배정
    confusion_vec.append(None)# None + 1 = Error

print(class_cnts,correct_cnts,confusion_vec )
for pred_idx in range(len(predictions)):
    pred = predictions[pred_idx]
    label = labels[pred_idx]
    class_cnts[label] += 1

    if pred == label:
        correct_cnts[label] += 1
print(correct_cnts)
print(class_cnts)
for class_idx in range(M_class):
    confusion_vec[class_idx] = correct_cnts[class_idx]/class_cnts[class_idx]
print('confusion vector: {}'.format(confusion_vec))


#
predictions = [0,1,0,2,1,2,0]
labels = [1,1,0,0,1,2,1]

n_class = None

for label in labels:
    if n_class == None or n_class < label:
        n_class = label
n_class += 1 # 인덱스가 0 부터 시작이기 때문에

class_cnts, correct_cnts, confusion_vec = list(), list(),list()
for _ in range(n_class):
    class_cnts.append(0)
    correct_cnts.append(0)
    confusion_vec.append(None)

for pred_idx in range(len(predictions)):
    pred = predictions[pred_idx]
    label = labels[pred_idx]

    class_cnts[label] += 1
    if pred == label:
        correct_cnts[label] += 1
for class_idx in range(n_class):
    confusion_vec[class_idx] = correct_cnts[class_idx]/class_cnts[class_idx]
print(f'confusion vector {confusion_vec}')


