a = ['caew', 'bde','adsr','abc']

# 첫문자열, 마지막문자열 순으로 정렬
def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))
print(sorted(a, key=lambda x:(x[0], x[-1])))