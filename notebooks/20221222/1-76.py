# 1-76 sorting

scores = [40,20, 30, 10, 50]
sorted_scores = list()

for _ in range(len(scores)): # 제일 큰 for 문
    M, M_inx = scores[0], 0

    for score_idx in range(len(scores)): # 현재 남아있는 scores에서 최대값 찾기
        if scores[score_idx] > M:
            M = scores[score_idx]
            M_inx = score_idx

    sorted_scores.append(M) # 찾은 최대값 삽입하기
    del scores[M_inx] # 삽입한 값 삭제

    print(f'remaining scores {scores}')
    print(f'sorted scores: {sorted_scores}')

#
print('000000000000000R')
scores = [20,40, 10, 50, 30]
sorted_scores = list()

for _ in range(len(scores)):
    M, M_idx = scores[0], 0

    for score_idx in range(len(scores)):
        if scores[score_idx] > M:
            M = scores[score_idx]
            M_idx =score_idx

    sorted_scores.append(M)
    del scores[M_idx]

    print('remaining scores {}'.format(scores))
    print('sorted scores {}'.format(sorted_scores))
