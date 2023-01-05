# 71번 방법의 단점
# 내가 데이터의 자료를 알고 있기 때문에 설정한 값 -> 그 외의 경우 에러가 잘 발생

scores = [-20,60,40,70,120]

# methd.1 원소의 첫번째 값으로 설정함

m, M = scores[0], scores[1]

for score in scores:
    if score > M :
        M = score
    if score < m:
        m = score

print(f'Man value : {M}, Min value : {m}')

# method.2 값을 None 으로 설정 -> 결국 한번 돌고나면 method.1 과 같다

m, M = None,None

for score in scores:
    if m == None or score < m :
        m = score
    if M == None or score >M:
        M = score
print(f'Man value : {M}, Min value : {m}')

