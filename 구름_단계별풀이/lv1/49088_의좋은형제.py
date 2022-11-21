'''
날짜: 2022.11.21
시간복잡도: O(100만)

문제: 
풀이: 
23:10~23:20

'''

first, last = map(int,input().split())
d = int(input())

flag = False
while d > 0:
    if flag==False: # 시작
        if first % 2 == 1: # 홀수
            temp = (first+1) // 2
        else:
            temp = first // 2
        first -= temp
        last += temp
        flag = True
    else:
        if last % 2 == 1: # 홀수
            temp = (last+1) // 2 
        else:
            temp = last // 2
        first += temp
        last -= temp
        flag = False
    
    d -= 1


print(first, last)

