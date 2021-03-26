import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 3

def cut(a, b, array, length):
    
    # 비교할 값을 찾고, 비교시작
    pre = array[a][b]
    for i in range(a, a+length):
        for j in range(b, b+length):
            if pre != array[i][j]:
                # 9등분한다.
                for x in range(3):
                    for y in range(3):
                        cut(a+length//3*x, b+length//3*y, array, length//3)
                # 봤으니까 리턴함
                return
    if pre == -1:
        result[0] += 1
    elif pre == 0:
        result[1] += 1
    elif pre == 1:
        result[2] += 1

cut(0, 0, data, n)
for i in result:
    print(i)