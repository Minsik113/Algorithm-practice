# # 파일열어 내용보기
# f = open('C:\\Users\\pc\\Desktop\\buy_list.txt', 'rt') # r = 읽기모드, t = 텍스트파일
# lines = f.readlines()
# print(lines)

# for line in lines:
#     print(line, end='')
# print()
# for line in lines:
#     nline = line.split('\n')[0]
#     print(nline)
# # print()

# # 파일에 글쓰기
# f = open('C:\\Users\\pc\\Desktop\\sell_list.txt', 'wt')
# f.write('삼성전자\n')
# f.write('하이닉스\n')
# f.close()

# 1~10까지 txt파일에 쓰기.
# f = open('C:\\Users\\pc\\Desktop\\sell_list.txt', 'wt') # 기존에 있던말던 첨부터 다시쓰기
# f = open('C:\\Users\\pc\\Desktop\\sell_list.txt', 'a') # 이어서쓰기
# for i in range(1,11):
#     a = str(i)+'\n'
#     f.write(a)

# 위에 코드를 python스럽게
# with open('C:\\Users\\pc\\Desktop\\sell_list.txt', 'a') as f:
#     for i in range(1,11):
#         a = str(i)+'\n'
#         f.write(a)