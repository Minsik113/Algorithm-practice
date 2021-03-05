########################################
########################################
# 보텀업 
'''
단순히 bfs에 모든 경우를 넣는거
나누거나 빼거나 2가지 경우로 분류해서 가장먼저 1에 도착하는 경우의 count 를 출력한다
-> bfs로 계속 보는거는 봤던 계산 또 해야한다.
-> 해쉬에 있다면 넘어가고, 없다면 해쉬에 넣고 q에 넣는식으로 해도 될 듯

메모이제이션 사용하자
=>d[i] = 'i를 1로 만드는데에 필요한 조건수의 최솟값'
'''
n = int(input())
d = [0] * 30001 # 30000개 같은거 반복적으로 계산됨

for i in range(2, n+1): 
    # 1을 빼는 경우
    d[i] = d[i-1] + 1 # 2 는 1이 되려면 1번이면 됨.
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])
########################################
########################################
# 탑다운 + bfs로 제일짧은길이 보기 
# => 이건 봤던 수 또 계산해야한다. 비효율적.
# from collections import deque
# n = int(input())

# q = deque()
# q.append((0,n))

# while q:
#     v = q.popleft()
#     level, num = v[0],v[1]
#     if num == 1:
#         print(level)
#         break
#     if num % 5 == 0:
#         q.append((level+1,num//5))
#     elif num % 3 == 0:
#         q.append((level+1,num//3))
#     elif num % 2 == 0:
#         q.append((level+1,num//2))
    
#     q.append((level+1,num-1))

