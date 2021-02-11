# 1/18
# 문제 난이도: Gold 5
# 문제 유형: 재귀
# 추천 풀이 시간: 40분

# 1. 자연수 N의 범위(3<=N<=9)가 매우 한정적이므로 완전 탐색으로 문제 해결가능
# 모든 경우를 다 계산하더라도 3^8 x test_Case수 임
# 2. 수의 리스트와 연산자 리스트를 분리하여 모든 경우를 계산하자.

# 가능한 모든 경우를 고려하여 연산자 리스트를 만드는 것이 관건이다.(재귀 이용)
# 파이썬의 eval()를 사용하여 문자열 형태의 표현식을 계산하자. evaluation
# ex) '2*3'이라는 문자열이있지만 이걸 6으로 계산해줌
#  1 + 2 3 이라면 24로 계산해줌

##################  ##################
# 백트래킹
test = int(input())

for i in range(test):
    N = int(input())
    numberarray = [i for i in range(1,N+1)]
    # n-1개의 operator들의 중복가능 모든경우 구해야함
    row = ['']*(N-1)
    data = [' ', '+', '-']
    operators = []

    def solve(depth):
        if depth == N-1:
            operators.append(''.join(map(str,row)))
            return
        for i in range(3):
            row[depth] = data[i] 
            solve(depth+1)
            row[depth] = 0

    def check(operators):
        for i in range(len(operators)):
            strings = ""
            for j in range(N-1):
                strings += str(numberarray[j]) + operators[i][j]
            strings += str(numberarray[-1])
            # ' ' 없앤 걸 eval해야함
            nstrings = strings.replace(" ","")
            if eval(nstrings) == 0:
                print(strings)
    
    solve(0)
    # string 조합하자. numberarray = int, operators = str
    check(operators)
    print()
##################  ##################
# product사용 - 중복허용되는 모든순열
from itertools import product

test = int(input())

for i in range(test):
    N = int(input())
    numberarray = [i for i in range(1,N+1)]
    # n-1개의 operator들의 중복가능 모든경우 구해야함
    row = ['']*(N-1)
    data = [' ', '+', '-']
    operators = list(product(data,repeat = N-1)) # ()로 저장되어있음

    for i in range(len(operators)):
        strings = ""
        for j in range(N-1):
            strings += str(numberarray[j]) + operators[i][j]
        strings += str(numberarray[-1])
        # ' ' 없앤 걸 eval해야함
        nstrings = strings.replace(" ","")
        if eval(nstrings) == 0:
            print(strings)
    
    print()
    

# 나동빈
import copy

def recursive(array, n):
    if len(array) == n: # array다 차면 return해줌. 계산해야하니까
        operators_list.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    integers = [i for i in range(1,n+1)]
    operators_list = []
    recursive([], n-1)

    # return 되어 나온 연산자들이 operators_list에 있음.
    #print(operators_list)

    for operators in operators_list:
        string = ""
        for i in range(n-1): 
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ","")) == 0:
            print(string)
    
    print()