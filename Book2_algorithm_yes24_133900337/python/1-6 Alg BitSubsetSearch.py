'''
날짜: 2024.10.28
시간복잡도: O(2^N * N)
문제: 비트완전탐색
방법: 모든 가능한 경우의 수를 비트 연산을 통해 탐색하는 알고리즘이다.
  부분 집합을 찾거나 조합을 구할 때 매우 효율적으로 사용할 수 있다. 특히 이진수를 이용해 각 경우의 수를 나타낼 수 있을때 유용하다.
  
  비트 완전 탐색의 개념
  1.비트 표현: 어떤 집합의 각 원소가 포함될지 여부를 비트로 표현합니다. 예를 들어,
    집합 {𝐴, 𝐵, 𝐶 }가 있을 때 이 집합의 부분 집합은 이진수 000부터 111까지 각 비트를 조합하여 나타낼 수 있습니다.
          000은 아무것도 선택하지 않는 경우
          001은 C만 선택하는 경우
          011은 B와 C를 선택하는 경우
          111은 A, B, C 모두 선택하는 경우
  2.전체 경우의 수: 길이가 𝑛인 집합이 있을 때, 가능한 부분 집합의 수는 2^n입니다. 이를 비트를 통해 효율적으로 생성할 수 있습니다.
    
  장점: 모든 경우의 수를 효율적으로 탐색 가능하며, 특히 집합의 크기가 작을 때 유용합니다.
  단점: 경우의 2^n수가 이므로, n이 클수록 시간 복잡도가 급격히 증가합니다.

'''
def bit_subset_search(arr):
  n = len(arr)
  all_subsets = []
  for i in range(1 << n): # 2^n 가지 경우의 수
    subset = []
    for j in range(n):
      # i의 j번째 비트가 1인지 확인하여 부분 집합에 포함
      if i & (1 << j):
        subset.append(arr[j])
    all_subsets.append(subset)
  return all_subsets

arr = ['A', 'B', 'C']
print(bit_subset_search(arr))

