'''
날짜: 2023.01.03
시간복잡도:

문제:
a/b 유한소수라면1, 무한소수라면2

풀이:
23:43~
기약분수로 나타냈을 때, 분모의 소인수가 2와 5만 존재해야한다.
1. a의 약수
2. b의 약수
3. 공통된거 제외하고 b의 약수가 2와 5만 존재하는지 확인
4. 그렇다면 1, 아니라면 2
'''
import math
def get_primes(n):
    # 구하고자 하는 수만큼 True를 갖는 리스트 생성
    is_primes = [True] * n
    # n의 최대 약수가 sqrt(n) 이하이므로 계산한 후, 소숫점이 있을 경우 올림으로 최대 반복 횟수 계산
    max_length = math.ceil(math.sqrt(n))

    for i in range(2, max_length):
        # True일 경우, 소수
        if is_primes[i]:
            # i이후 i의 배수들을 지워나감
            for j in range(i + i, n, i):
                is_primes[j] = False

    # 리스트의 True로 남아 있는 인덱스(소수)를 추출
    return [i for i in range(2, n) if is_primes[i]]

def solution(a, b):
    answer = 0
    print(get_primes(b))
    # a_save = [1,a]
    # b_save = [1,b]
    # for i in range(2, int(a**(1/2))+1):
    #     if a % i == 0:
    #         a_save.append(i)
    #         a_save.append(a//i)
    # print(a_save)
    return answer