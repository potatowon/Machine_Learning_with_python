# 1-71
# n배수들의 합 구하기

multiple_of = 3

numbers = list()
for num in range(100):
    numbers.append(num)

sum_multiple_on_n = 0
for num in numbers:
    if num % multiple_of == 0:
        sum_multiple_on_n += num
print(sum_multiple_on_n)

# 5배수들의 합 구하기

multiple_of = 5

numbers =list()
for num in range(100):
    numbers.append(num)

sum_multiple_on_n = 0
for num in numbers:
    if num % multiple_of ==0:
        sum_multiple_on_n += num
print(sum_multiple_on_n)
