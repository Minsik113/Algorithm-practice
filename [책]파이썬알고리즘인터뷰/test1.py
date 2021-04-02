a = ["wer w a x d f", "wrax 1 3 4 2","wer w a x d f", "wrax 1 3 4 2"]
for log in a:
    if log.split()[1].isdigit():
        print(log,'숫자임')
    else:
        print(log,'알파벳임')
# b = [4, 5, 6]
# print(a+b)