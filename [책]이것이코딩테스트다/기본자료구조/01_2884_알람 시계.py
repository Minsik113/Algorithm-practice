h, m = list(map(int, input().split(' ')))
if m < 45:
    if h > 0:
        h = h - 1
    else:
        h = 23
    
    m = m + 60 - 45

else:
    m = m - 45

print(h, m)

    

    