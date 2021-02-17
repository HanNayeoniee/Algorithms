"""
백준 5717. 상근이의 친구들
problem : https://www.acmicpc.net/problem/5717
"""

while(1):
    M, F = map(int, input().split())
    if (M == 0 and F == 0):
        break
    print(M+F)
