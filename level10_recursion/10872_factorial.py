# 백준 10단계 1번 - 팩토리얼
# 재귀를 사용해 팩토리얼 구현하기

def factorial(n):
    if (n==0):
        return 1
    else:
        return (n * factorial(n-1))

num = int(input())
res = factorial(num)
print(res)