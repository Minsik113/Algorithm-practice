'''
날짜: 2025.04.02
링크: https://school.programmers.co.kr/learn/courses/30/lessons/161990?language=python3
시간복잡도: O(N^2)

1.학습키워드
구현, 2차배열

2.문제
극단의 좌표 4개를 구한다. 최상단 제일오른쪽 최하단 제일왼쪽
(최상단,제일왼쪽) ~ (최하단,제일오른쪽) 을 이으면 최소로 잡을 수 있는 사각형이 된다.

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
각 극단의 좌표를 구한다. 최하단과 제일오른쪽은 각각+1씩해줘야한다. 파일의 길이가 1이므로 (0,1)에 파일이있다면 (1,2)에 대각좌표가 위치한다.

4.어떻게 해결했는지
단순하게 반복문사용. 구현은 어렵지 않으나 문제를 이해했는지가 중요한문제이다.

5.무엇을 새롭게 알았는지

#99클럽 #TIL #개발자취업 #코딩테스트준비 #코테연습 #항해99 #코테

'''
def solution(wallpaper):
    #1.변수선언
    rtop = 999  # top과 rleft는 좌표값이 제일 작은애들이다 min 
    rleft = 999
    rbottom = -1 # right와 bottom은 좌표값이 제일 큰애들이다 max
    rright = -1 
    
    #2. 그린다
    for i in range(len(wallpaper)): #상하
        for j in range(len(wallpaper[0])): #좌우
            if wallpaper[i][j] == "#":
                rtop = min(rtop, i)
                rleft = min(rleft, j)
                rbottom = max(rbottom, i+1)
                rright = max(rright, j+1)
    
    return [rtop, rleft, rbottom, rright]
