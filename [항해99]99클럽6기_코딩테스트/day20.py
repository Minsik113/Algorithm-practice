'''
날짜: 2025.04.27
링크: https://www.acmicpc.net/problem/17265
시간복잡도: O(N*N) ??

1.학습키워드
최단거리, 그리디

2.문제
(1,1)에서 (N,N)으로 최단거리로 이동할때 최댓값과 최솟값을 구하라.(3<=N<=5)

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
모든경우를 다 따져보자.
  
4.어떻게 해결했는지
dfs
  
5.무엇을 새롭게 알았는지


'''
import sys
input=sys.stdin.readline

def dfs(i:int, j:int, cur_num:str, before:str):
    global max_answer, min_answer
    
    if i == n-1 and j == n-1:
        max_answer = max(max_answer, int(cur_num))
        min_answer = min(min_answer, int(cur_num))
    
    for k in range(2):
        nx = i+dx[k]
        ny = j+dy[k]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[nx][ny].isdigit():
            dfs(nx,ny,str(eval(cur_num+before+board[nx][ny])),'')
        else:
            dfs(nx,ny,cur_num,board[nx][ny])

# 1.입력받기
n = int(input())
board = [ list(input().split()) for _ in range(n)]
dx = (1,0)
dy = (0,1)
max_answer = -1e9
min_answer = 1e9
dfs(0,0,board[0][0],'')
print(max_answer,min_answer)