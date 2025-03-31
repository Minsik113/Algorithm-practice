'''
날짜: 2025.03.31
링크: https://www.acmicpc.net/problem/1929
시간복잡도: O(N**2 루트2)

1.학습키워드
소수(prime number) : 정수론에서 소수는 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수다.

2.문제
m~n사이의 소수개수를 구해라

3.어떤 문제가 있었고, 나는 어떤 시도를 했는지
- m~n까지의 수 중 소수인 수들을 모두 출력하는 문제이고, 1~1,000,000까지 가능하기에 시간복잡도를 전부 다 확인하면 시간초과가 나온다. 즉, 시간초과를 해결해야한다.
- 에라토스테네스의 채 알고리즘을 알고있었으나, 오랜만의 코딩이라그런지 구현이 잘 되지 않았다. 생각한걸 구현가능할수있게 연습!
  
4.어떻게 해결했는지
- 약수관계로 절반까지만 보는법. O(N^2 / 2)가 되므로 안됨.
- 소수판별법. O(N^2)의 루트2라서 가능할듯. 
- 에라토스테네스의 체 방식. O(N * log log N)
  
5.무엇을 새롭게 알았는지
소수 구하는 방법과 인간은 기억력이 좋지 않다는 것😱

'''

import math

# 2이상 자연수 소수 판별
def is_prime_number(x):
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return False
  return True

m, n = map(int, input().split())

for i in range(m,n+1):
  if i == 1:
    continue
  if(is_prime_number(i)):
    print(i)


