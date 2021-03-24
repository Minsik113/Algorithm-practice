while True:
    s = []
    flag = True
    string = input()
    # 종료조건
    if string == '.': 
        break
    # 
    for i in string:
        if i == '(' or i == '[':
            s.append(i)
        elif i == ')':
            if not s or s[-1] == '[':
                flag = False
                break
            elif s[-1] == '(':
                s.pop()
        elif i == ']':
            if not s or s[-1] == '(':
                flag = False
                break
            elif s[-1] == '[':
                s.pop()
    if flag and (not s): # flag == True and s가비어있으면yes
        print("yes")
    else:
        print("no")

        
