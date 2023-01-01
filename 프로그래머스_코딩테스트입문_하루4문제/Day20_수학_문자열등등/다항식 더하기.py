'''
날짜: 23.01.01
시간복잡도:

문제:
풀이:
23:20~23:34
x가 몇번나왔나 체크
'''
def solution(polynomial):
    answer = ''
    p = polynomial.replace(" ","").split("+")
    
    cntx = 0
    cnt = 0
    for i in p:
        if 'x' in i:
            if len(i) == 1:
                cntx += 1
            else:
                cntx += int(i[0])
        else:
            cnt += int(i)
    # print(cntx, cnt)
    if cntx == 0 and cnt == 0:
        return 0
    if cntx != 0:
        answer = str(cntx) +"x"
    if cnt != 0:
        answer += " + " + str(cnt)
    return answer