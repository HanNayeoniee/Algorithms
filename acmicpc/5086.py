"""
백준 5086. 배수와 약수
problem : https://www.acmicpc.net/problem/5086
"""

while(1):
    num1, num2 = map(int, input().split())
    if (num1 == 0 and num2 == 0):
        break
    if (num2%num1 ==0):
        print("factor")
    elif (num1%num2 == 0):
        print("multiple")
    else:
        print("neither")
