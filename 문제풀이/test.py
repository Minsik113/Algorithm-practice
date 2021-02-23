'''
00 00 00 
~
N 59 59 
까지 3이 하나라도 포함되면 경우의 수 증가.

모든 경우의 수는? 

24 x 60 x 60
'''

n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in (str(i)+str(j)+str(k)):
                count += 1
print(count)
