# 1-79 Histogram 구하기

scores = [50,20,30,40,10,50, 70,80,90,20,30]
cutoff = [0,20,40,60,80] # 각 구간
histogram = [0]*5

for score in scores:
    if score > cutoff[4]:
        histogram[4] += 1
    elif score > cutoff[3]:
        histogram[3] += 1
    elif score > cutoff[2]:
        histogram[2] += 1
    elif score > cutoff[1]:
        histogram[1] += 1
    elif score > cutoff[0]:
        histogram[0] += 1
    else:
        pass

print(f'histogram of the sores: {histogram}')


histogram = [0]*5
for score in scores:
    if score > cutoff[4]:
        histogram[4] += 1
    elif score > cutoff[3]:
        histogram[3] +=1
    elif score > cutoff[2]:
        histogram[2]  += 1
    elif score > cutoff[1]:
        histogram[1] += 1
    elif score > cutoff[0]:
        histogram[0] += 1
    else:
        pass

print(histogram)

