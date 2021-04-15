import random

TRIALS = 10000000 # 1억 
same_birthdays = 0

for z in range(TRIALS):
    birthdays = []
    # 23명이 모였을 때 생일이 같은 경우 same_birthdays + 1
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)
    print(z, same_birthdays)
print(f'{same_birthdays / TRIALS * 100} %')