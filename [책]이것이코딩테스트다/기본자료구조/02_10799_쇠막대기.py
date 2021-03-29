# 1/14
# 걸린시간: 30분

# 허공에 레이저 쏘는 경우
#   개수 안늘어남
# 파이프에 레이저 쏘는 경우

pipe = list(map(str, input()))

l_count = 0 
answer = 0 

for i in range(0,len(pipe)):
    if pipe[i] == '(': # '('
        l_count += 1  
    elif i > 0 and pipe[i-1] == '(' and pipe[i] ==')': # 레이저
        l_count -= 1
        answer += l_count
    elif i > 0 and pipe[i] == ')': # ')' = 1개
        l_count -= 1
        answer += 1
    else: # 시작부터 ')' 나오는 경우
        print("error")
        exit(0)

print(answer)

################ 
################
# 스택이용
# 하나씩 넣으면서 본다

x = list(input())

s = []
count = 0

for i in range(0,len(x)):
    if x[i] == '(': # '('일 때
        s.append('(')
    
    else: # ')'일때 1.레이저, 2.끝부분
        if x[i-1] == '(': # 레이저
            s.pop()
            count += len(s)
        else: # 끝부분
            s.pop()
            count += 1
print(count)


