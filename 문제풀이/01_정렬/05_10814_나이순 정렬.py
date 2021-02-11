# 1/15
# 문제 유형: 정렬
# 추천 풀이 시간: 15분

# 나이 이름
# 나이: 오름차순 
# 나이 같으면) 먼저 가입한 순서대로

import sys
x = int(sys.stdin.readline())

data = []

for _ in range(x):
    a, b = sys.stdin.readline().rstrip().split(' ')
    data.append((int(a),b))

data.sort(key=lambda x: x[0]) 
# 나이로 sort하겠다. 그 외 요소는 들어온 순서대로 됨.

for i in data:
    print(i[0], i[1])

# 동빈나

# (나이, 이름)의 정보를 입력받은 뒤에 나이를 기준으로 정렬
# 기본 정렬 라이브러리를 이용
# 나이 동일) key속성을 설정

n = int(input())
array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array.sort(key=lambda x: x[0])

print(array)