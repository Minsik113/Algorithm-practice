####################
# 날짜: 2023.10.16
# 시간복잡도:
# 해결시간: 00:01~00:12
# 포인트:
# input의 각자리의 값 * (base ** 자릿수위치)
#3번풀이보면된다.
# 
####################

#1. 처음풀이. -> 파이썬스럽지 않음. 
num, base = map(int, input().strip().split(' '))

idx = 0
answer = 0
strNum = str(num)
for i in range(len(strNum), 0, -1):
    answer += int(strNum[i-1]) * (base**idx)
    idx+=1
print(answer)

#2. 1번보다 간단히. 하지만 역시 파이썬스럽진않음 -> enumerate함수를 이용해서 위보다 간단하게 풀기
num, base = map(int, input().strip().split(' '))

answer = 0
num = str(num)
for idx, number in enumerate(num[::-1]):
    answer += int(number) * (base **idx)
print(answer)

#3. 파이썬 내장함수 사용. ->  int(x, base=진수)
num, base = map(int, input().strip().split(' '))

answer = int(str(num), base)
print(answer)