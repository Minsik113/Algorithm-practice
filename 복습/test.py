'''
그냥 짝이 아니면 no라고하면된다. 
짜증나네
'''

s = []
flag = True
while True:
    string = input()
    for i in range(len(string)):
        # 열음
        if string[i] == '(' or string[i] == '[':
            s.append(string[i])
        # 닫음
        elif string[i] == ')':
            # 1. 짝이 아니니까 no이다. '.'나올때까지 보자
            if len(s) == 0: 
                # print("1") 
                flag = False
            else:
                k = s.pop()
                if k != '(':
                    # print("2")
                    flag = False
        # 닫음
        elif string[i] == ']':
            # 2. 짝이 아니니까 no이다. '.'나올때까지 보자
            if len(s) == 0: 
                # print("3") 
                flag = False
            else:
                k = s.pop()
                if k != '[':
                    # print("4")
                    flag = False
        elif string[i] == '.':
            # 3번. 짝이 안맞음 => no
            if not flag: 
                print("no") 
            # 4번. 짝맞음 => 길이가 남아있으면 no임
            elif len(s) != 0: 
                print("no") 
            # 5번. 짝맞음 => 길이가 0이면 yes지
            else:
                print("yes")
            # print(s,flag)
            s = [] # 스택초기화                
            flag = True # flag초기화
