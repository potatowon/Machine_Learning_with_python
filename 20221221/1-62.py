# 1-62
# 초를 분초로 표현하기

seconds = 200

if seconds >= 60:
    minutes = seconds//60
    seconds -= minutes*60
else:
    minutes = 0
print(f'{minutes} minutes {seconds} sec')

seconds = 500

if seconds > 60:
    minutes = seconds//60
    seconds -= minutes*60
else:
    minutes = 0
print(f'{minutes} minutes {seconds} sec')

seconds = 39

if seconds >= 60:
    minutes = seconds//60
    seconds -= minutes*60

else:
    minutes = 0
print(f'{minutes} minutes {seconds} sec')