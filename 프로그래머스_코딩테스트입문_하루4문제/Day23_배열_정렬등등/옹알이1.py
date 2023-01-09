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