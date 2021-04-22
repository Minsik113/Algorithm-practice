##########################################
##########################################
# 4/22 - 계차수열 + 스택 
# 맨아래풀이가 제일 간단해 보임.
n = int(input())
array = list(map(int, input().split()))
count = [0] * (n+1) # 1~n까지의 공포도

for i in array:
    count[i] += 1

s = []
result = 0
for i in range(1, n+1):
    if count[i] != 0:
        for j in range(count[i]):
            s.append(i)

        # 팀으로 묶을 수 있는 애들은 다 뺴라
        while (len(s) // i) > 0:
            for j in range(i):
                s.pop()
            result += 1
print(result)

##########################################
##########################################
# 내풀이 - 계차수열사용
'''
작은애들있으면 작은애들끼리 숫자맞춰서 보내면된다.
n = 10만이니까 계차로 개수센후 하나씩 그룹만든다
'''
n = int(input())
array = list(map(int, input().split()))
count = [0] * (n+1)
for i in range(n):
    count[array[i]] += 1

# 그룹원이 다 차면 바로 보낸다.
result = 0 # 답
save = 0 # 이월되는 잉여
for i in range(1, n+1): # count에 대해서 보면된다.
    num = count[i] // i # 보낼 수 있는 그룹 수
    gar = count[i] % i + save # 잉여인원과 현재 남아야하는 인원 합한수
    # 잉여합한게 보낼 수 있는 그룹원이 만들어졌다면 보낸다
    if gar >= i:
        num += 1
        save = gar - i # 나머지를 이월시킴
    # 잉여합한게 그룹못만들면 이월시킴
    else:
        save = gar
    result += num
print(result)
##########################################
##########################################
# sort()사용
'''
그리디. 
1. 입력받은 array리스트 정렬한다
2. 하나씩 개수 센다.(count)
3. pos가 한칸씩 이동한다.
4. 개수 == array[pos] 라면 result +=1 and count = 0
5. pos가 끝에 도달할 때까지 보면 된다.
=> 최소한의 모험가로 최대팀을 꾸려 모험할 수 있다.
'''

n = int(input())
array = list(map(int, input().split()))
array.sort()

count = 0 # 현재 그룹원 수
result = 0 # 총 그룹 수

# 공포도가 낮은애부터 확인한다
for i in array:
    count += 1
    if count >= i: #포함된 모험가의 수가 공포도 이상이라면, 그룹결성
        result += 1
        count = 0

print(result)
