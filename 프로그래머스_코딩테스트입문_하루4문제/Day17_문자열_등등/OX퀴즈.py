'''
날짜: 2022.12.23
시간복잡도:

문제:
=을 기준으로 나눈다. 왼쪽결과가 오른쪽이랑 같은지 비교

풀이:
22:10~22:16(6분)

'''
def solution(quiz):
    answer = []
    for q in quiz:
        cal, res = q.split("=") # 계산식, 결과
        if eval(cal) == int(res.replace(' ','')):
            answer.append("O")
        else:
            answer.append("X")
    return answer