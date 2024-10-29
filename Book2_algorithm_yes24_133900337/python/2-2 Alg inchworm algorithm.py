'''
날짜: 2024.10.29
시간복잡도: O()
시간: 21:41~
문제: A07 Event Attendance
  1.x~y일까지 참여한 참석자수를 구해야한다.
  2.d일동안 n명이 방문하였다.
  3.n번 참가자는 R일~L일을 참석하였다  
  4.1~d일 동안 참여한 참석자수는?
풀이방식:   
  1<=D<=100000, 1<=N<=100000 이라서 모든 수 카운팅하면 시간초과.
  부분합으로접근.
  
  
'''

d = int(input())
n = int(input())

# 1~d일까지 참여자 수를 카운팅하겠다.
s = [0] * (d+1) 
for _ in range(n):
  x, y = map(int, input().split()) 
  s[x] += 1   # x일에 들어오고
  s[y+1] -= 1 # y일에나가니까

arr = [0] * (d+1)
for i in range(1, len(s)):
  arr[i] = arr[i-1] + s[i]
print(s)
print(arr)
  
