# 1-70

numbers = list()

for num in range(20):
    numbers.append(num)

numbers.append(3.14)
print(numbers)

for num in numbers:
    if num % 2 == 0:
        print('Even')
    elif num % 2 == 1:
        print('Odd')
    else:
        print('not an Integer')