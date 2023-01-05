# 1 - 59
# 숫자 빈도 구하기

numbers = [0,2,4,2,1,4,3,1,2,3,4,1,2,3,4]
number_cnt = [0]*5

for num in numbers:
    number_cnt[num] += 1
print(number_cnt)

numbers = [0,2,4,2,1,4,3,1,2,3,4,1,2,3,4]
number_cnt = [0,0,0,0,0]

for num in numbers:
    number_cnt[num] += 1
print(number_cnt)

numbers = [0,2,4,2,1,4,3,1,2,3,4,1,2,3,4]
number_cnt = [0]*5

for num in numbers:
    number_cnt[num] += 1
print(number_cnt)