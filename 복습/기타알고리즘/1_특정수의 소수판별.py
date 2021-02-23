'''
● 문제: K라는 수가 약수인지 체크하자.

1) O(K)
: K이하의 수로 다 나눠보는것

2) O(K루트2)
: 약수를 이용하자. K의 가운데 약수까지 확인하면 뒤쪽은 안봐도 됨.


'''
import math 

# 소수 판별 함수
def is_prime_number(x):
    # 2 ~ x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x))+1):
        # x가 i로 나누어 떨어진다면 소수가아님
        if x % i == 0:
            return False
    return True

print(is_prime_number(10))
print(is_prime_number(31))



