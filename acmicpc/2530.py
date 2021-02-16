"""
백준 2530. 인공지능 시계
problem : https://www.acmicpc.net/problem/2530
"""

hour, minute, sec = map(int, input().split())
timer = int(input())

sec += timer
minute += sec //60
hour += minute //60

sec %= 60
minute %= 60
hour %= 24
        
print(hour, minute, sec)
