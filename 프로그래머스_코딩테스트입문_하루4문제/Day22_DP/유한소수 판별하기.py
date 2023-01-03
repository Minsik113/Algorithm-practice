'''
날짜: 2023.01.03
시간복잡도:

문제:
a/b 유한소수라면1, 무한소수라면2

풀이:
23:43~
기약분수로 나타냈을 때, 분모의 소인수가 2와 5만 존재해야한다.
1. a의 약수
2. b의 약수
3. 공통된거 제외하고 b의 약수가 2와 5만 존재하는지 확인
4. 그렇다면 1, 아니라면 2
'''
def solution(a, b):
    answer = 0
    # 원래 값 저장
    real_a = a; real_b = b
    
    a_save = []
    n = 1
    while a > 1:
        n += 1
        # print(real_a,a,n)
        if a % n == 0:
            if real_a == n:
                break
            else:
                a_save.append(n)
                a = a//n 
                n = 1
    print('a',a_save)
    
    b_save = []
    n = 1
    while b > 1:
        n += 1
        # print(real_b,b,n)
        if b % n == 0:
            if real_b == n:
                break
            else:
                b_save.append(n)
                b = b//n 
                n = 1
    print('b',b_save)
    if real_b % real_a == 0:
        b_save.remove(real_a)
    print('b',b_save)
        
    test = set()
    for i in b_save:
        if i not in a_save:
            test.add(i)
    print(">>>",test)
    test -= {2}
    test -= {5}
    print(test,len(test))
    if len(test) == 0:
        return 1
    return 2
