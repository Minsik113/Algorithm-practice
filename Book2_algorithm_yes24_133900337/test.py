n,x = map(int, input().split())
arr = list(map(int, input().split()))
flag = False
for i in arr:
    if x==i:
        print("Yes")
        flag = True
        break
if not flag:
    print("No")