# min max 구하기

scores = [60, 40, 70,20, 30]
M, m = 0, 100

for score in scores:
    if score > M:
        M = score
    if score < m:
        m = score
print(f'Max value: {M}')
print(f'Min value: {m}')

#

m, M = 100, 0

for score in scores:
    if score > M:
        M = score
    if score < m:
        m = score
print(f'Max value: {M}, Min value: {m}')