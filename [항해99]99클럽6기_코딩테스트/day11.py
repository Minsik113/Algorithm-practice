'''
날짜: 2025.04.14 19:20~
링크: https://www.acmicpc.net/problem/16401
시간복잡도: 

1.학습키워드
이분탐색. 정렬

2.문제
m명의조카, n개의과자. 조카에게 반드시 같은 길이의 막대 과자를 줘야한다.
조카1명에게 줄 수 있는 막대과자의 최대 길이는? 단, 과자를 자를순있지만 합치는건 안됨

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
M과 N이 100만이라 O(NlogN)이하로 해야한다.

4.어떻게 해결했는지
정렬해놓고 하나씩 넣기엔 고려해야할게 너무 많다.
경우의 수를 다 파악하는 그리디의 경우에도 자른막대가 다른막대보다 길 수가 있어서 고려해야할게 너무 많다.
힌트를 봐버렸다. => 이분탐색
 1)1부터 제일큰수 사이의 중간값A를 구한다. 
 2)A로 n명을 나누어줄 수 있다면 A와 제일큰수사이의 중간값으로 다시.
 3)그렇지 않다면 1과 A의 중간값으로 다시.

5.무엇을 새롭게 알았는지
이분탐색

#99클럽 #TIL #개발자취업 #코딩테스트준비 #코테연습 #항해99 #코테

'''
m, n = map(int,input().split())
arr = list(map(int, input().split()))
start = 1
end = max(arr) # 제일큰애
result = 0
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in range(n):
        cnt += arr[i]//mid # 이 길이로 과자를 여러개 만들 수 있음
    
    if cnt >= m:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
        
print(result)