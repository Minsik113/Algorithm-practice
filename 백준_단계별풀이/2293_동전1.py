'''
n가지동전 합이 k
n=100 k=10000

코인 수 제한 없음.  
[1,2,5]코인이있음 k = 10

1 1 1 1 1

'''
n, k = map(int, input().split())
coins = [int(input()) for x in range(n)]

