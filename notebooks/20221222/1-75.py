# 1-75 최댓값과 최솟값의 위치 구하기

scores = [60, -20, 40, 120, 70]
m, M = scores[0], scores[0]
m_idx , M_idx = 0,0

for score_idx in range(len(scores)):
    score = scores[score_idx]
    if M < score:
        M = score
        M_idx = score_idx
    if score < m :
        m = score
        m_idx = score_idx
print(f'M/M_idx : {M},{M_idx}')
print(f'm/m_idx : {m},{m_idx}')