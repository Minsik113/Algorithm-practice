'''
날짜: 2022.12.26 -> 2023.01.01
시간복잡도:

문제:
직사각형 넓이 구하기

풀이:
23:38~
두 변의 곱 -> 직사각형의 변 // 좌표평면축 (평행)

방법1
1. 한 점에서 나머지 세 점까지의 거리를 각각 구한다.
2. 가장 긴 길이는 뺀다. 대각선이니까
3. 남은 두 길이의 곱이 넓이
방법2
x,y로 sorted해라
1. 가장 긴애를 구해라 -> 오른쪽 위
2. 가장 작은애 -> 왼쪽 아래 
3. 두 변 길이 구할 수 있겠지.
'''
def solution(dots):
    dots = sorted(dots,key=lambda x:(x[0],x[1]))  # idx[0],idx[3]가 대각선임
    '''
    1 2
    3 4 로 구분한다고할때 sorted(x축,y축하면) 3 1 4 2 순서로 나옴
    '''
    a = dots[1][1] - dots[0][1]
    b = dots[2][0] - dots[0][0]
    return a*b

def solution(dots):
    dots = sorted(dots,key=lambda x:(x[0],x[1]))  # idx[0],idx[3]가 대각선임
    x = dots[0][0]
    y = dots[0][1]
    ax = dots[1][0]
    ay = dots[1][1]
    bx = dots[2][0]
    by = dots[2][1]
    
    a = int(((x-ax)**2+(y-ay)**2)**(1/2))
    b = int(((x-bx)**2+(y-by)**2)**(1/2))
    # print(a,b)
        
    return a*b