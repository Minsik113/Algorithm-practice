'''
날짜:2022.12.09
시간복잡도:

문제:
풀이:
1. 1부터 약수의 개수를 센다.단, 약수의 개수가 2개 나오면, 그 수의 배수는 모두 합성수임

1은 모두의 약수, 자기자신은 항상 약수


'''
def solution(n):
    answer = 0
    a = [0]*101 # 약수개수 1~100
    
    a[1] = 1
    for i in range(2,101):
        cnt = 1 # 1은 항상 약수니까
        if a[i] == 0:
            for j in range(2,i+1):
                if i % j == 0: # 나누어지면 
                    cnt += 1
            a[i] = cnt
            t = 1
            while True:
                if i*t > 100:
                    break
                a[i*t] = cnt*t
                t+=1
    
    for i in range(n+1):
        if a[i] >= 3:
            answer+=1
    return answer