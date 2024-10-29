'''
날짜: 2024.10.29
시간복잡도: O(N)
시간: 20:50 ~ 21:23
문제: A06 How Many Guests?
풀이방식: 
  1. n일동안 a~b일사이에 방문한 사람들의 수는? 이 질문을 q번 하겠다.
    ㄴSn이 1일에서 n일까지 방문한 사람들이라고 한다면, Sb - S(a-1) = a~b일동안 방문자

'''

n, q = map(int, input().split())
arr = list(map(int, input().split()))
# 부분합 구할 날짜 입력받기. none으로 입력해두니 직관적이네
l = [None] * n
r = [None] * n
for i in range(q):
  l[i], r[i] = map(int, input().split())

# 부분합 Sn구하기. 1~n일까지의 방문객 수 
s = [None] * (n+1)
s[0] = 0
for i in range(n):
  s[i+1] = s[i]+arr[i]
  
print(s)
for i in range(q):
  print(s[r[i]]-s[l[i]-1])
  
  
  