'''
dp[i,j] = (i,j)위치에서 의 (값,행위치)를 저장
1. 열이 1증가할때, 이전행에서 -1 0 1 만큼 이동가능하다
2. 열이 끝까지 도달했을 때 값의 최대값을 고르면 됨

1. dp[]
'''
test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    d = [[(0,0)]*n for _ in range(m)] # 
    print(d)


