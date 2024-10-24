'''
날짜: 2024.10.24
시간복잡도:O(N^2)

문제: A03 Two Cards
풀이방식: 
  q와 p의 모든경우를 더해서 합이 K가 나오는지 보기. 
  N이 최대100이라 완전탐색으로 풀면됨. 최대 O(100^2)
  
  N이 엄청크다면? 
  우선 순서대로 정렬로 만든다 O(2NlogN)
  p는 작은거부터 + q는 큰거부터 본다.크기를비교한다
  1.if p+q < K, 더 큰걸 더해야하니까 parr[p+1]+q[maxlength-1] 로 한다
  2.if p+q > K, 작은애를 더해야하므로 parr[p+1]+q[maxlenght-2] 로 한다.
  1과2를 p+q == K 일 때까지 반복하면됨.
'''
n, k = map(int, input().split())
parr = list(map(int, input().split()))
qarr = list(map(int, input().split()))
flag = False

for i in parr:
    if flag:
        break
    for j in qarr:
        if (i+j) == k:
            print("Yes")
            flag = True
            break

if not flag:
    print("No")