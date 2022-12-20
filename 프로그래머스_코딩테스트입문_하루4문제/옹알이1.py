'''
날짜: 2022.12.20
시간복잡도:

문제:
주어진 옹알이들 중, 4개 단어 조합으로 이루어진 옹알이의 개수는?

풀이:
17:28~17:38(10분)
방법1.replace('단어',숫자)
 숫자로 대체해서 전부다 숫자로 이루어졌다면 통과.
방법2.replace('단어',' ')
 공백이 되면 끝
'''
def solution(babbling):
    answer = 0
    dic = ["aya","ye","woo","ma"]
    for babble in babbling:
        for eng in dic:
            babble = babble.replace(eng,' ')
        # 모든게 숫자로 이루어졌다면 통과
        # print('>>',"babble:",babble,"len(babble):",len(babble))
        if len(babble.strip()) == 0:
            # print('>>>>',"babble.strip():",babble.strip(),"len(babble):",len(babble.strip()))
            answer += 1
    return answer

def solution(babbling):
    answer = 0
    dic = ["aya","ye","woo","ma"]
    for babble in babbling:
        for idx,eng in enumerate(dic):
            if babble.count(eng) != 0:
                babble = babble.replace(eng,str(idx))
                
        # 모든게 숫자로 이루어졌다면 통과
        print(babble)
        if babble.isdigit():
            answer += 1
    return answer