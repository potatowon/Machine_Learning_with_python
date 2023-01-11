import numpy as np
import matplotlib.pyplot as plt
# 1번
'''
fig = plt.figure(figsize=(7,7), facecolor='linen')
plt.show()

fig = plt.figure(figsize=(7,7), facecolor='orange')
ax = fig.add_subplot()

plt.show()
'''
#2번
'''
fig = plt.figure(figsize=(7,7), facecolor='linen')
ax = fig.add_subplot()
# ax.plot([2,3,1]) # 하나만 적을 경우 x 값을 자동적으로 0,1,2,... 으로 인식
ax.scatter([2,3,1],[2,3,4]) #(x,y) 값으로 선정
plt.show()
'''
# 3번
'''
# figsize = (7,7) 따로 변수를 지정해도 무관함
fig, ax = plt.subplots(figsize=(7,7))
plt.show()
'''

# 4번 페이지의 제목 지정하기
'''
figsize = (7,7)
fig, ax = plt.subplots(figsize=figsize)
#fig.suptitle("Title of a Figure")

#fig.suptitle("Title of a Figure", fontsize=30)
#plt.show()

fig.suptitle("Title of a Figure", fontsize = 30, fontfamily='monospace')
plt.show()
'''

# 5번 그래프의 이름 지정하기
'''
figsize =(7,7)
fig, ax = plt.subplots(figsize=figsize)
ax.set_title("Title of a Ax", fontsize=30, fontfamily='serif')

plt.show()
'''

#6번 라벨에 이름 달기
'''
figsize = (7,7)
fig, ax = plt.subplots(figsize=figsize) # 하나의 ax(axes:공간중내가 사용할 부분) 만을 가지는 하나의 figure 생성

ax.set_xlabel("X label", fontsize=30)
ax.set_ylabel("Y label", fontsize=30)
plt.show()
'''

# 7번 색상 지정하기, alpha 투명도 조절하기

'''
figsize = (7,7)
fig, ax = plt.subplots(figsize=figsize)
fig.suptitle("Title of a Figure",fontsize=10)
ax.set_title("Title of a Ax", fontsize=30, fontfamily='monospace')
ax.set_xlabel('X label', fontsize=20, color='darkblue', alpha=0.7)
ax.set_ylabel("Y label", fontsize=20, color='red', alpha=0.7)

plt.show()

figsize =(7,7)
fig, ax = plt.subplots(figsize=figsize)
fig.suptitle("Title of Figure", fontsize=20)
ax.set_title('Title of a Ax', fontsize=30, color='green', alpha=1)
ax.set_xlabel("X label", fontsize=20, color='darkblue', alpha=0.3) # 숫자가 작을 수록 연해짐
ax.set_ylabel("Y label", fontsize=20, color='black', alpha=0.6)

plt.show()
'''

# 8번 alpha 값 연습
'''
figsize = (7,7)

fig, ax = plt.subplots(figsize=figsize)

fig.suptitle("Title of Figure", fontsize=30, color='darkblue', alpha=0.9)
ax.set_title("Title of a Ax", fontsize=20, color='darkblue', alpha=0.7)
ax.set_xlabel("X label", fontsize=20, color='darkblue', alpha=0.5)
ax.set_ylabel("Y label", fontsize=20, color='darkblue', alpha=0.3)
fig.tight_layout() # 상하좌우 여백을 없애주는 역할
plt.show()
'''

# 9번 상하좌우 여백 없애기 fig.tight_layout()
    # 사이즈를 맞게 조정하는 역할도 함

# 10번 축 추가 ax.twinx / 축의 범위 set_xlim([0,100])

# fig = plt.figure(figsize=(7,7))
#
# ax1 = fig.add_subplot()
# ax2 = ax1.twinx()
#
# ax1.set_xlim([0,100])
#
# ax1.set_ylim([0,100])
# ax2.set_ylim([0,0.1])
#
# fig.tight_layout()
# plt.show()



# 11번

fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot()
ax2 = ax1.twinx()

ax1.set_xlim([0,100])
ax1.set_ylim([0,100])
ax2.set_ylim([0,0.1])

ax1.set_title("Twinx Graph", fontsize=30)
ax1.set_ylabel("Data1", fontsize=20)
ax2.set_ylabel("Data2", fontsize=20)

fig.tight_layout()
plt.show()



# 12-1번 ax.tick_parmas : 축에 나타내지는 숫자 Labelsize Argument
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.tick_params(labelsize=15)
plt.show()
'''

# 12-2번 tick length and width arguments
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.tick_params(labelsize=20,
               length = 10,
               width=3)
plt.show()
'''

# 12-3번 tick값 제거
    # bottom : 아래 tick 의 유무
    # labelbottom : 숫자의 유무
    # left : 왼쪽의 tick의 유무
    # leftbottom : 왼쪽 tick의 숫자 유무
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.tick_params(labelsize=20,
               length=10,
               width=3,
               left=False,
               labelleft=False)
plt.show()
'''

# 12-4번 tick 과 label을 옮기기
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.tick_params(labelsize=20,
               length=10,
               width=2,
               bottom=False, labelbottom=False,
               top=True, labeltop= True,
               left=False, labelleft=False,
               right=True, labelright=True)
plt.show()
'''
# 12-5 tick, label rotation -> 기본 반시계 방향의 회전
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.tick_params(labelsize=20,
               length=10,
               width=3,
               rotation=30)
plt.show()
'''
# 12-6 번 tick 과 label 설정을 축 별로 설정
     # axis = 'x' , axis = 'y'
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.tick_params(axis = 'y',
               labelsize=20,
               length=10,
               width=3,
               rotation=30)
plt.show()
'''
# 13번 Grid
    # ax.text() : text 내용의 추가
    # ax.grid()

'''
figsize =(7,7)
fig, ax = plt.subplots(figsize=figsize)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])

ax.grid() # grid 성정
ax.tick_params(axis='both',
               labelsize=15
               ) # both는 안써도 상관없음
ax.text(x=0, y=0,
        s='hello',
        fontsize=30)
# alignment는 기본이 우측상단임

plt.show()
'''

# 14-1번 Text Alignment(x,y location)
        # basic : va='bottom', ha='left'
'''
figsize =(7,7)
fig, ax = plt.subplots(figsize=figsize)

ax.set_xlim([-1,1])
ax.set_ylim([-1,1])

ax.grid()

ax.text(x=0, y=0,
        s='Hello1',
        fontsize=30)

ax.text(x=0.5, y=0,
        s="Hello2",
        fontsize=30)

ax.text(x=0.5, y=-0.5,
        s= "Hello3",
        fontsize=30)
plt.show()
'''

# 14-2 번 Text Aligment(Alignments Arguments)
    # horizontal alingment -> ha
    # vertical alignment -> va
'''
fig, ax = plt.subplots(figsize=(7,7))

ax.grid()
# ha="left" 필요 없는 값
ax.text(x=0, y=0,
        va ="center", ha="right",
        s="Hello",
        fontsize=30)

plt.show()
'''
#14-3 번 va Alignment
'''
fig, ax = plt.subplots(figsize=(7,7))
ax.grid()
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.text(x=0, y=0,
        s= "Hello",
        va='center', ha='center',
        fontsize=30)
plt.show()
'''
# 연습1
'''
figsize = (7,7)

fig, ax = plt.subplots(figsize=figsize)
ax.set_xlim([-1,1])
ax.set_ylim([-1,1])
ax.grid()

ax.text(x=0, y=0,
        s="Hello",
        va='bottom', ha="right",
        fontsize=20)
# plt.show()

ax.text(x=0, y=0,
        s="Hello",
        ha="left",
        fontsize=20)

ax.text(x=0,y=0,
        s="Hello",
        ha='right', va='top',
        fontsize=20)
ax.text(x=0, y=0,
        s="Hello",
        ha="left", va="top",
        fontsize=20)
plt.show()
'''

# 연습2
'''
fig, ax = plt.subplots(figsize=(7,7))
ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.grid()

ax.text(x=4, y=4,
        va='top', ha='right',
        s = "Hello2",
        fontsize=20)
ax.text(x=-4, y=4,
        va='top', ha='left',
        s = "Hello1",
        fontsize=20)
ax.text(x=4, y=-4,
        va='bottom', ha='right',
        s = "Hello4",
        fontsize=20)
ax.text(x=-4, y=-4,
        va='bottom', ha='left',
        s = "Hello2",
        fontsize=20)
plt.tight_layout()
plt.show()
'''

# 15번 ax.set_xticks(Arbitrary Locations)
        # 원하는 tick 값을 직접 설정할 수 있다.
'''
fig, ax = plt.subplots(figsize=(7,7))
ax.set_xlim([0,10])
ax.set_ylim([0,1])

ax.set_xticks([0,1,5,10])

plt.show()
'''

# 15-2 ax.set_xticks(labelsize Argument)  -> 리스트 변수로 지정해서 tick의 값을 설정할 수 있다.
'''
fig, ax = plt.subplots(figsize=(7,7))

xticks = [i for i in range(10)]
ax.set_xticks(xticks)
ax.tick_params(labelsize=20)
plt.show()
'''

# 15-3번 ax.set_xticks(Regular Intervals)
'''
fig, ax = plt.subplots(figsize=(7,7))
xticks = [i for i in range(0,101,20)]

ax.set_xticks(xticks)
ax.tick_params(axis='x',
               labelsize=20,
               length=20,
               width=3,
               rotation=30)
plt.show()
'''

# 15-4 Major and Minor Ticks
         # minor tick의 경우 따로 지정해 주는 과정이 필요하다.
'''
fig, ax = plt.subplots(figsize=(7,7))

major_xticks = [i for i in range(0,101,20)]
minor_xticks = [i for i in range(0, 101, 5)]

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True) # minor tick임을 지정해준다

ax.tick_params(axis='x',
               labelsize=20,
               length=10,
               width=3,
               rotation=30)
ax.tick_params(axis='x',
               which='minor',
               length=5,
               width=2
               )
plt.show()
'''

# 연습

# fig, ax = plt.subplots(figsize=(7,7))
# major_xticks = [i for i in range(0,101,20)]
# minor_xticks = [i for i in range(0,101,5)]
#
# major_yticks = [j for j in range(0,11,2)]
# minor_yticks = [j for j in range(0,11,1)]
#
# ax.set_xticks(major_xticks)
# ax.set_xticks(minor_xticks, minor=True)
#
# ax.set_yticks(major_yticks)
# ax.set_yticks(minor_yticks, minor=True)
#
# ax.tick_params(axis='x',
#                  labelsize=20,
#                  length=10,
#                  width=3,
#                  rotation=30)
# ax.tick_params(axis='x',
#                  which='minor',
#                  length=5,
#                  width =2)
#
# ax.tick_params(axis='y',
#                  labelsize=20,
#                  length=10,
#                  width=3)
# ax.tick_params(axis='y',
#                which='minor',
#                 length=4,
#                 width=2)
#
# plt.show()