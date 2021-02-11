''' 백트래킹은 완전탐색, BFS, DFS와 유사하다.
# 2/2
# 문제 난이도: Gold 5
# 문제 유형: 백트래킹
# 추천 풀이 시간: 30분

C개의 문자들 중에서 L개를 선택하는 '모든 조합'을 고려해야 한다.
-> python의 조합(combinations) Library를 사용하면 간단히 해결가능
-> 혹은 DFS를 이용하여 조합 함수를 구현할 수 있다.

모든 조합가능한 경우를 구한 후, 모음 자음 개수를 세자.
'''

############## ##############
# 나동빈 - combination 라이브러리 사용
from itertools import combinations

vowels = ('a','e','i','o','u')
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 정렬 수행
array = input().split()
array.sort()
# print(array)

# 길이가 L인 모든 암호 조합을 확인
for password in combinations(array, l):
    # 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    # 최소 한 개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and count + 2 <= l:
        print(''.join(password))