from dataclasses import dataclass
import pprint

class Product:
    weight: int = None
    price: float = None
apple = Product()
apple.price = 10
print(apple.price)

def fin(a):
    pass

def fin1(a: int) -> bool:
    pass

########
orginal = dict()
a = {}
for key, value in orginal.items():
    a[key] = value

a = {key: value for key, value in orginal.items()}
########
# def get_natural_number():
#     n = 0
#     while True:
#         n += 1
#         yield n
# g = get_natural_number()
# for _ in range(0, 100):
#     print(next(g))

x = 1; z = 2
print(f'{x+1}하잇{z}')

pprint.pprint(locals())

a = 10
b = a 
print(a, b)
print(id(a), id(b))
b = 15
print(id(a), id(b))

a = [1, 2, 3, 4, 4, 5, 6, 7]
print(a.index(4))
a = dict()
a = {
    'key1': 'value1'
    , 'key2': 'value2'
}
a['key3'] = 'value3'
try:
    print(a['key4'])
except:
    print('존재하지 않는 키')
print(a)
#######
import collections
a = [1, 2, 3, 4, 5, 6, 5, 5, 5, 6]
b = collections.Counter(a)
print(b)
print(b.most_common(2)) # 가장 빈도가 높은거 2개를 선택

