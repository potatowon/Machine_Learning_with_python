# 1-63
# 초를 시분초로 표현하기

seconds = 5000

if seconds >= 3600:
    hours = seconds//3600
    seconds -= hours*3600
else:
    hours = 0
if  seconds >= 60:
    minutes = seconds//60
    seconds -= minutes*60
else:
    minutes = 0

print(f'{hours} hours {minutes} minutes {seconds} sec')

# 시분초

seconds = 39428

if seconds >= 3600:
    hours = seconds//3600
    seconds -= hours*3600
else:
    hours = 0

if seconds >= 60:
    minutes = seconds//60
    seconds -= minutes*60
else:
    minutes = 0

print(f'{hours} hours {minutes} min {seconds} sec')

seconds = 364

if seconds>= 3600:
    hours = seconds//3600
    seconds -= hours*3600
else:
    hours = 0

if  seconds >= 60:
    minutes = seconds//60
    seconds -= minutes*60
else:
    minutes = 0
print(f'{hours} hours {minutes} minutes {seconds} sec')