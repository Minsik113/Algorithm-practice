# 1/15
# 문제 유형: 정렬
# 추천 풀이 시간: 15분

# 1/ (x,y)를 입력 받은 뒤, x, y순서대로 차례대로 오름차순 정렬
# 2/ '기본 정렬 라이브러리'는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬한다.
# 3/ 따라서 단순히 기본 정렬 라이브러리를 이용하면 된다(key 속성 설정 없이)
import sys

x = int(sys.stdin.readline())
data = []

for _ in range(x):
    a, b = sys.stdin.readline().split(' ')
    data.append((int(a),int(b)))

data.sort()

for i in data:
    print(i[0], i[1])

# 동빈나

n = int(input())

array = []

for _ in range(n):
    x, y = map(int, input().split(' '))
    array.append((x, y))

array.sort()

for i in array:
    print(i[0], i[1])



            
    
            