# 1-74

# Min_Max Nomalization

scores = [-20, 60, 40, 70 ,120]

m, M = scores[0], scores[0]
for score in scores:
    if score > M :
        M = score
    if score < m:
        m = score

for score_idx in range(len(scores)):
    scores[score_idx] = (scores[score_idx] - m)/(M -m)

print(" scores after normaliztion : \n ", scores)

m, M = scores[0], scores[0]
for score in scores:
    if score > M :
        M = score
    if score < m:
        m = score
print(f'Max : {M}, min: : {m}')

#

# 최대 최소 구하기

M, m = scores[0], scores[0]

for score in scores:
    if score > M:
        M = score
    if score < m:
        m = score

for score_idx in range(len(scores)):
    scores[score_idx] = (scores[score_idx] - m)/(M-m)
print("score after normalization : \n", scores)

M, m = scores[0], scores[0]

for score in scores:
    if score > M :
        M = score
    if score < m:
        m = score

print(f'Max : {M}, Min : {m}')