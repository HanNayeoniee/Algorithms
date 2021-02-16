"""
백준 2525. 오븐 시계
problem : https://www.acmicpc.net/problem/2525
"""

hour, minute= map(int, input().split())
timer = int(input())

hour += timer // 60
minute += timer % 60

if(minute >=60):
    hour += 1
    minute -= 60
if(hour >= 24):
    hour -= 24
        
print(hour, minute)
