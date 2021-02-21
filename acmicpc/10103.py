"""
백준 10103. 주사위 게임
problem : https://www.acmicpc.net/problem/10103
"""

case = int(input())
p1 = 100
p2 = 100

for i in range(case):   
    num1, num2 = map(int, input().split())

    if (num1 > num2):
        p2 -= num1
    elif (num1 < num2):
        p1 -= num2    
    
print(p1)
print(p2)    
