"""
백준 2914. 저작권
problem : https://www.acmicpc.net/problem/2914
"""

songs, avg = map(int, input().split())
res = songs * (avg-1) + 1
print(res)
