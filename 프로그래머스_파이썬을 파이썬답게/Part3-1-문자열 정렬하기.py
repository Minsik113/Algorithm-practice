####################
# 날짜: 2023.10.25
# 시간복잡도: O(1)
# 해결시간: 10분
# 포인트:
# 
#
#
####################

# 1.눈에 보이는대로 출력하기 - 처음풀이
# s, n = input().strip().split(' ')
# n = int(n)
# sLen = len(s)

# print(s)
# print(" "*((n-sLen)//2)+s)
# print(" "*(n-sLen)+s)

# 2.ljust, center, rjust 사용
s = "가나다라"
n = 7
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))
import string
print(string.ascii_lowercase) # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits 