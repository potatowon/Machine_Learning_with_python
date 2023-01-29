# correlation : 원소별로 더해서 합!

'''
window 를 쭉 뽑으면서, 내가 원하는 패턴이 있는 부분만 추출하는 연산

 - data 에서 window를 뽑고, filter와 내적한 결과를 저장
 - window 와 filter가 같을 때 가장 큰 값을 출력
 - window 와filter가 반대 벡터일 때 가장 작은 값을 출력


딥러닝의 CNN과 동작 기작이 비슷하다.

nomalization -> 데이터 전처리과정에서 해결
이미지의 경우는 0 ~ 255 이고 / 255 를 해주는 nomalization 을 하기도 함.
'''

import numpy as np

np.random.seed(0)

data = np.random.randint(-1, 2, (10, )) # 튜플이므로, 10 한개만 적을때는 10, 로 기재 -> 한개만 적으면 1, 10 이다.

filter_ = np.array([-1, 1, -1])

print(f"{data = }")
print(f"{filter_ = }")

L = len(data)
F = len(filter_)

L_ = L - F + 1
filtered = []

for idx in range(L_):
    window = data[idx: idx+F]
    filtered.append(np.dot(window, filter_))

filtered = np.array(filtered)

print("filtering result:", filtered)
