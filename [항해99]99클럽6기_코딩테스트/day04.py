'''
날짜: 2025.04.03
링크: https://www.acmicpc.net/problem/2468
시간복잡도: O(최고높이 x N x N)

1.학습키워드
bfs

2.문제
물에 잠기지않은 땅을 이어서 하나의 대륙을 만든다. 
물의 높이는 1~max(대륙높이)까지 가능하다. 제일 많은 대륙을 만들 수 있을때 그 개수는?

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
상하좌우를 따라가 물에 잠긴지 확인해야한다.
물의 높이가 1~max값에따라 안전지대가 몇곳인지 확인해라. 이중 제일 많은 안전지대가 나오는 경우, 그 안전지대 개수를 써라

4.어떻게 해결했는지
bfs를 구현. 1부터 땅의 최고 높이까지 물의 높이를 설정해가며 테스트한다.
변하지 않는 맵을 하나 두고, 유동적으로 바꿀수있는 맵을 만들어놔야한다.

5.무엇을 새롭게 알았는지
bfs기억이 가물가물했는데 풀어보면서 기억을 상기해 볼 수 있어 좋았습니다.
'''

# 1.그리기
n = int(input())
real_nums = [list(map(int, input().split())) for _ in range(n)]
result = [] # 각 높이별 대륙의개수

# 2. 최고높이구하기
top = 0
for i in range(n):
    for j in range(n):
        top = max(top, real_nums[i][j])
        
# 3.BFS구현
dx = [-1, 0, 1, 0] # 위오아왼
dy = [0, 1, 0, -1]
q = []

for k in range(1, top+1):
    cnt = 0  # 높이가 k일때 대륙개수
    nums = [[real_nums[i][j] for j in range(n)] for i in range(n)] # 맵닦기
    
    for i in range(n):
        for j in range(n):
            if nums[i][j] >= k: # k이상이면 안전한 땅이므로 대륙을 만들자
                q.append([i,j])
                nums[i][j] = -1 # 안전한땅
                while q:
                    a, b = q.pop()
                    for x in range(4):
                        nx = a + dx[x]
                        ny = b + dy[x]
                        if nx >= n or nx < 0 or ny >= n or ny < 0: # 봤던땅이거나 범위를 벗어나면 다음걸보자. 
                            continue
                        #print((i,j), (nx,ny))
                        if nums[nx][ny] >= k: # 조건에 맞으면 (dx,dy)도 가봐야함. 스택(또는 큐)에 추가
                            q.append([nx,ny])
                            nums[nx][ny] = -1 # 안전한땅
                cnt += 1#연결된 모든 경우를 다 봤다면 카운트증가
                
    result.append(cnt)
    
    
##for i in range(n):
##    for j in range(n):
##        print(nums[i][j],end=' ')
##    print(end='\n')
print(max(result))
