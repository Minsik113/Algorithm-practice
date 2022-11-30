def solution(price):
    answer = 0
    if price < 100000:
        answer=price
    elif 100000<=price and price<300000:
        answer=0.95*price
    elif 300000<=price and price<500000:
        answer=0.9*price
    else:
        answer=0.8*price
    return int(answer)

# dictionary로 선언해놓고 해도됨

