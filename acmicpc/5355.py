"""
백준 5355. 화성 수학
problem : https://www.acmicpc.net/problem/5355
"""

case = int(input())

for i in range(case):
    numbers = list(map(str, input().split()))
    res = float(numbers[0])
    j = 1
    
    for j in range(len(numbers)):
        if(numbers[j] == '@'):
            res *= 3

        if(numbers[j] == '%'):
            res += 5

        if(numbers[j] == '#'):
            res -= 7
            
    print("{:.2f}".format(res))
