'''
# 1/31
# 문제 난이도: Bronze 2
# 문제 유형: 그리디
# 추천 풀이 시간: 10분

단순히 '큰 화폐 단위' 순서대로 잔돈을 거슬러 주면 최적의 해를 얻음
'''


n = int(input())
data = [500,100,50,10,5,1]
pos = 0
result = 0
n = 1000 - n
while n > 0:
     # 500
    if n >= data[pos]: 
        n -= data[pos]
        result += 1
    else:
        pos += 1
print(result)
############  ############
# 나동빈
changes = 1000 - int(input())
count = 0 
for i in [500,100,50,10,5,1]:
    count += changes//i
    changes %= i
print(count)
