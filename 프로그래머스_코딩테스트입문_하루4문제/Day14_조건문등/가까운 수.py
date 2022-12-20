'''
날짜: 2022.12.20
시간복잡도: O(N)

문제:
풀이:
15:58~16:05 (7분)

방법1
무조건 모든 수를 다 봐야함. O(N)
 정렬O(NlogN)할 필요가 없음. 어차피 다 볼거니까. 
 각 수와 n의 차이를 변수에 저장해두자
  O(N)으로 끝
방법2
그냥 정렬해서 풀어도 쉬움
'''
def solution(array, n):
    answer = 0
    minvalue = 99999
    for i in range(len(array)):
        temp = abs(n-array[i])
        if temp < minvalue: # 더 작은게 나오면 바꿔준다
            minvalue = temp
            answer = i
        elif temp == minvalue: # 값이 동일하면, 더 작은 수로 바꿈
            minvalue = temp
            if array[i] < array[answer]:
                answer = i
    return array[answer]