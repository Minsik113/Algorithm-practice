# 1/14 
# 문제유형: 해시, 구현 
# 추천 풀이 시간: 15분

# hash.sha256(문자열의 바이트 객체).hexdigest(): 해시 결과 문자열

import hashlib
import sys

test = sys.stdin.readline().rstrip()

result = hashlib.sha256(test.encode())

print(result.hexdigest())

# 동빈나
import hashlib

data = input()
encoded_data = data.encode()
result = hashlib.sha256(encoded_data).hexdigest()

print(result)
