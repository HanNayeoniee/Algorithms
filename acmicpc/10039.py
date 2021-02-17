"""
백준 10039. 평균 점수
problem : https://www.acmicpc.net/problem/10039
"""

score = []
total = 0

for i in range(5):
    i = int(input())
    
    if (i<40):
        i = 40
    score.append(i)
    total += i
    
print(total//5)
