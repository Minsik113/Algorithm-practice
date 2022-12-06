'''
날짜: 2022.12.06
시간복잡도:

문제:
풀이:
풀이1
1. len(numbers) == 짝수면 같은수만 반복됨
2. len(numbers) == 홀수면 두번돌고 반복됨

풀이2
그냥 다 넣어도됨
k가 1000까지인데 한 칸 건너뛰니까, 2000개이상의 배열로 채우면됨
12 34 56 12 34 56 k=5 3
'''
def solution(numbers, k):
    answer = 0
    arr = []
    while True:
        if len(arr) > 2000:
            break
        arr.extend(numbers)
    return arr[2*k-2]

def solution(numbers, k):
    return numbers[2*(k-1) % len(numbers)]

    