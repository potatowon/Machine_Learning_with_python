# 1-77
# string 에서 ', " 를 사용하는 경우는 영어에서 '를 사용하는 경우가 잦기 때문이다.

# Accuracy
# 모델이 예측한 값과 실제 값을 비교하여 잘 모델링 되어있는지 평가

predictions =[0,1,0,2,1,2,0]
labels = [1,1,0,0,1,2,1]
n_correct = 0

for pred_idx in range(len(predictions)):
    if predictions[pred_idx] == labels[pred_idx]:
        n_correct += 1

accuracy = n_correct/len(predictions)
print('accuracy[%]: {} %'.format(accuracy*100))

predictions =[0,1,0,2,1,2,0]
labels = [1,1,0,0,1,2,1]
n_correct = 0

for pred_idx in range(len(predictions)):
    if predictions[pred_idx]== labels[pred_idx]:
        n_correct += 1
accuracy = n_correct /len(predictions)
print(f'accuracy[%]: {accuracy*100} %')

