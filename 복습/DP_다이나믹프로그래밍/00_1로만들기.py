'''
n이라는 수를 1로만들고싶어한다. 
1. 4가지규칙이 있으며
2. 1이되면 연산횟수 출력
-> 1부터 숫자에 따른 연산회수를 저장해서 같은수를 또 계산하지 않는다.
(메모이제이션사용) ㄴㄴ시간초과.

=>26부터 / or -1 을 보면서 bfs로 1발견하면 출력.

'''
########################################
########################################
# 보텀업 
n = int(input())
d = [0] * 30001

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[n])
########################################
########################################
# 탑다운 + bfs로 제일짧은길이 보기
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

