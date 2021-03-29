# 1/14
# 걸린시간:

# 1/ ‘()’ 인 괄호열의 값은 2이다.
# 2/ ‘[]’ 인 괄호열의 값은 3이다.
# 3/ ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# 4/ ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 5/ 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산


###########
###########
###########

data = list(input())
s = []
count = 0

for i in data:
    if i == ')':
        t = 0
        while len(s) != 0: # '))', '숫자)', 에러
            top = s.pop()
            if top == '(': # ()
                if t == 0:
                    s.append(2)
                else:
                    s.append(2*t)
                break
            elif top == '[': # 에러
                print(0)
                exit(0)
            else: # 숫자)
                t = t + int(top)
    
    elif i ==']':
        t = 0
        while len(s) != 0: # '))', '숫자)', 에러
            top = s.pop()
            if top == '[': # ()
                if t == 0:
                    s.append(3)
                else:
                    s.append(3*t)
                break
            elif top == '(': # 에러
                print(0)
                exit(0)
            else: # 숫자)
                t = t + int(top)
    
    else:
        s.append(i)

for i in s:
    if i =='(' or i =='[':
        print(0)
        exit(0)
    else:
        count += i # ex. [2,18,...] 은 다 더해야함

print(count)
