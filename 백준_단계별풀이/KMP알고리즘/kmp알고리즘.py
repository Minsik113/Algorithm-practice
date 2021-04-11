# part = 'CTCACTGCCTGCCTACTGCCTACTGCCTAC'
part = 'CTGCCTAC'
size_ = len(part)
table = [0] * size_

for i in range(1, size_):
    # KMP 실행
    j = 0

    while j > 0 and part[i] != part[j]:
        j = table[j-1]
    
    if part[i] == part[j]:
        j += 1
        table[i] = j
print(table)
