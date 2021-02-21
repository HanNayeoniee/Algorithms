"""
백준 2476. 주사위 게임
problem : https://www.acmicpc.net/problem/2476
"""

case = int(input())
res_list = []

for i in range(case):
    res = 0
    num_list = list(map(int, input().split()))

    for i in range(3):
        if (num_list.count(num_list[i]) == 3):
            res = 10000 + num_list[0]*1000
        if (num_list.count(num_list[i]) == 2):
            res = 1000 + num_list[i]*100
        if (num_list.count(num_list[i]) == 1):
            res = max(num)*100
    res_list.append(res)

print(max(res_list))
