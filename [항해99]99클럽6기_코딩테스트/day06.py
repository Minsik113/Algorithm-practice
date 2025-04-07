'''
날짜: 2025.04.07
링크: https://www.acmicpc.net/problem/4963
시간복잡도: O(WH)

1.학습키워드
bfs

2.문제
섬과 바다로 맵이 주어지는데, 섬의 개수를 구하라.

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
bfs를 구현하면 된다. 4방위가아니라 8방위로 작성해야한다

4.어떻게 해결했는지
bfs구현

5.무엇을 새롭게 알았는지

섬, 유기농 백준문제풀어보기

'''

while(True):
    w, h = map(int, input().split()) # 너비 높이
    if(w == 0 and h == 0): break
    
    #1.맵그리기 1:땅 0:바다
    nums = [list(map(int,input().split())) for _ in range(h)]

    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
    cnt = 0
    q = []
    #2. bfs
    for i in range(h):
        for j in range(w):
            if nums[i][j] == 1:
                q.append([i,j])
                nums[i][j] = 2
                while q:
                    a, b = q.pop()
                    for x in range(9):
                        nx = a + dx[x]
                        ny = b + dy[x]
                        if nx < 0 or ny < 0 or nx >= h or ny >= w:
                            continue
                        if nums[nx][ny] == 1:
                            q.append([nx,ny])
                            nums[nx][ny] = 2
                cnt += 1
    print(cnt)