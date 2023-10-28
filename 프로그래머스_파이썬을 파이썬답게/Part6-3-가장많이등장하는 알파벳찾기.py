####################
# 날짜: 2023.10.28
# 시간복잡도: O(NlogN)
# 해결시간: 6분 (21:02~21:08)
# 포인트:
# 1.우선 개수를 세자. 세면서 제일 큰 값 업데이트 O(N)
# 2.제일 큰 값을 가진애들 쭉 보기 O(N)
# 3.소팅 O(NlogN)
####################

# 문제 - 가장 많이 등장하는 알파벳만을 사전순으로 출력

# 1. 하나씩 세자. O(NlogN)
my_str = input().strip()
dictStr = dict()
maxNum = 0
answer = []
for i in my_str:
    if i not in dictStr:
        dictStr[i] = 1
    else:
        dictStr[i] += 1
    maxNum = max(maxNum, dictStr[i])

for s, idx in dictStr.items():
    if idx == maxNum:
        answer.append(s)

# print(dictStr) # {'d': 3, 'f': 3, 'e': 1, 'g': 1}
print(''.join(sorted(answer))) # df


# 2. Counter함수를 사용해서 쉽게 접근가능.
import collections
my_str = input().strip()
answer = collections.Counter(my_str)

print(answer) # {'d': 3, 'f': 3, 'e': 1, 'g': 1}
for s, idx in answer.items():
    print(s,idx)