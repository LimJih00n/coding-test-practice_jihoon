#백준 2747 
'''
피보나치 수열 구하기 using dp
하다가 충격받아서 바로 시작함.
'''
fib_map = {}
def fib(n):
    if n==0:
        return 0
    if n not in fib_map:
        fib_map[n] =fib(n-1) + fib(n-2) 
    return fib_map[n]
fib_map[1]=1
fib_map[2]=1
n = int(input())
print(fib(n))