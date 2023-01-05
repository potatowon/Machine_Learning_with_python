# 절댓값 구하기

numbers = [-2,2,-1,3,-4,9]
abs_numbers = list()

for num in numbers:
    if num < 0:
        abs_numbers.append(-num)
    else:
        abs_numbers.append(num)
print(abs_numbers)

abs_numbers = list()

for num in numbers:
    if num < 0:
        abs_numbers.append(-num)
    else:
        abs_numbers.append(num)
print(abs_numbers)

abs_numbers = list()

abs_numbers = [ -num  if num < 0 else num for num in numbers]
print(abs_numbers)