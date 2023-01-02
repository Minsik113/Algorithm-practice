'''
날짜: 2023.01.02
시간복잡도: O(N^2)

문제:
풀이:
20:32~20:40(8분)
지뢰1,땅0
'''
def solution(board):
    answer = 0
    # 북 북동  동 남동  남 남서 서  북서 
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny]==2 or board[nx][ny]==1:
                        continue
                    # 땅이라면 건설
                    board[nx][ny] = 2
    # 땅 세기
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer+=1
    return answer