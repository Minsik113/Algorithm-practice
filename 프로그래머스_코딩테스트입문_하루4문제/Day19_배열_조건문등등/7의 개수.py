'''
날짜: 2022.12.25
시간복잡도: O(6 * 100) # 자릿수(6) * 원소개수(100)

문제:
배열에 7이 총 몇개있는지 찾기

풀이:
20:42~20:45(3분)
1.string으로 변환한다.
2.7의 개수 카운팅
3.배열의 원소를 다 볼때까지 끝날때까지 1,2반복
'''
def solution(array):
    return str(array).count('7')

def solution(array):
    answer = 0
    for i in array:
        for j in str(i):
            if j == '7':
                answer += 1
    return answer