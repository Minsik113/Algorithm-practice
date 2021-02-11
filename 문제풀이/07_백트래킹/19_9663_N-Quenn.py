''' 백트래킹은 완전탐색, BFS, DFS와 유사하다.
# 1/31
# 문제 난이도: Gold 5
# 문제 유형: 백트래킹
# 추천 풀이 시간: 40분

대표적인 백트래킹(Kacktracking) 문제이다.
가능한 경우를 전부 탐색하면서 더이상 나아갈 수 없는 경우를 만났을 때,
 이전으로 돌아가서 다시 다른 경우를 탐색하는 문제
DFS를 이용하여 백트래킹 알고리즘을 간단히 구현가능
'''
n = int(input())
row = [0] * n
result = 0

def solve(depth):
    global result
    if depth == n:
        result += 1
        return
    for i in range(n):
        row[depth] = i
        if check(depth):
            solve(depth+1)
def check(depth):
    for i in range(depth):
        if row[depth] == row[i]:
            return False
        if abs(row[depth] - row[i]) == depth - i:
            return False
    return True
    # (1,1) 과 (3,3)은 x축 (3-1=2)차이. y축(3-1=2)차이가 나기때문에 대각선이다.
    # 반면에 (1,1)과 (3,2)는 x축(3-2)차이 y축(3-1=1)차이가 나기떄문에 대각선이 아니다.
    # 좌표그려보면 명확해진다.
    # 즉, 두 좌표의 x축과 y축 각각 차이가 같은 곳인지만 보면된다.
solve(0)
print(result)

############ ###########
# 동빈나
# x번째 행에 놓은 Queen에 대해서 검증
def check(x):
    # 이전 행에서 놓았던 모든 Queen들을 확인
    for i in range(x):
        # 위쪽 or 대각선을 확인
        if row[x] == row[i]: # 같은 열에 퀸이 있다
            return False
        if abs(row[x] - row[i]) == x - i:
            return False
    return True

# x번쨰 행에 대하여 처리
def dfs(x):
    global result
    if x == n:
        result += 1
    else:
        # x번째 행의 각 열에 Queen을 둔다고 가정
        for i in range(n):
            row[x] = i
            # 해당 위치에 Queen을 두어도 괜찮은 경우
            if check(x):
                # 다음 행으로 넘어가기
                dfs(x + 1)

n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)