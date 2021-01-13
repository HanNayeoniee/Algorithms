# 백준 10단계 2번 - 피보나치 수 5
# 재귀를 사용해 피보나치 수 구현하기

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fib(n-1) + fib(n-2))

num = int(input())
res = fib(num)
print(res)