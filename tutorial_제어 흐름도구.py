words = ['cat','window','dog']

for w in words:
    print(w,len(w))
    
for i in range(0,5):
    print(i)
    
for i in range(len(words)):
    print(i, words[i])
    
    
sum(range(5,5))

# 2~50 까지 소수찾기
for n in range(2,51):
    for x in range(2,n):
        if n % x == 0: #나누어지면
            print(n,'equals',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')

# 피보나치 수열 만들기
def fib(n): # n까지 피보나치수열 리스트로 만들기
    a,b = 0,1
    result = []
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result
a=fib(10)


def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def concat(*args, sep="/"):
     return sep.join(args)
concat("abc","wer","swer")

list(range(3,5))
args=[3,5]
list(range(*args))

def make(n):
    return lambda x: x+n

f= make(42)
f(1)

pairs = [(1,'one'),(4,'four'),(2,'two'),(3,'three')]
pairs.sort(key=lambda pair:pair[1])

def my_function():
    """Do nothing, but document it,
    
    No, really, it doesn't do anything.
    """
    a=1
    b=3
    a+b

print(my_function.__doc__)
