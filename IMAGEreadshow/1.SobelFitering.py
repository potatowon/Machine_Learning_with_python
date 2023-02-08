import numpy as np
import matplotlib.pyplot as plt

''' np.ones : 입력된 shape의 array를 만들고 모두 1로 채워주는 함수 '''
tmp = np.ones(shape=(2, 3)) # (2, 3)의 shape 을 가지고 모두 1로 채워져있는 행렬을 만든다.
print(tmp, '\n')  # '\n' 다음 출력값에 한줄 뛰기

'''ndarray에 Scalar 곱을 하면 원소별 곱셈 '''

tmp2 = 10*tmp
print(tmp2)
