# 1/19
# 문제 난이도: Silver 4
# 문제 유형: 탐색
# 추천 풀이 시간: 20분

# 문서의길이 최대 2500. 단어의 길이 최대 50
# 단순히 모든경우를 다 한다고해도 NxM이니까 2500x50 = 10만정도
# O(NM)으로 시간안에 해결됨.

##########################  ##########################
import sys

text = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

idx = 0 # 움직일 포인트
count = 0 # 나온 횟수

while len(text)-idx >= len(word):
    if text[idx: idx+len(word)] == word:
        count += 1
        idx += len(word)
    else:
        idx += 1

print(count)

##########################  ##########################
# 동빈나

document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index: index + len(word)] == word: # 찾으면
        result += 1
        index += len(word)
    else: # 현재 위치에없으면 옆으로 이동
        index += 1
print(result)

