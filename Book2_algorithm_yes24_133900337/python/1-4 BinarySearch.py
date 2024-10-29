'''
날짜: 2024.10.24
시간복잡도:

문제: A04 Binary Representation
풀이방식: 
  1. n이 1이 될때까지 2로 나눈다.
  2. 나머지들을 저장해놓고 LIFO방식으로출력하면될듯(stack)

  =======================================================
  =========================심화==========================
  Q. n이 음수도된다면?

'''
#비트연산자 사용해서 풀어보자

#내풀이
n = int(input()) # n은 양수로 가정하자
m = n
arr = ""
while (m>1):
  r = m%2
  m = m//2
  if r == 0:
    arr = "0" + arr
  else:
    arr = "1" + arr
if m == 1:
  arr = "1" + arr
print(arr)

a = 13
print(a<<2)