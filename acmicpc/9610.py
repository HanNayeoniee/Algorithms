"""
백준 9610. 사분면
problem : https://www.acmicpc.net/problem/9610
"""

case = int(input())
res = [0]*5  # 순서대로 Q1, Q2, Q3, Q4, AXIS

for i in range(case):
    nums = list(map(int, input().split()))
    x = nums[0]
    y = nums[1]
    
    if (x*y == 0):
        res[4] += 1
    elif (x>0 and y>0):
        res[0] += 1
    elif (x<0 and y>0):
        res[1] += 1
    elif (x<0 and y<0):
        res[2] += 1
    elif (x>0 and y<0):
        res[3] += 1

print("Q1:", res[0])
print("Q2:", res[1])
print("Q3:", res[2])
print("Q4:", res[3])
print("AXIS:", res[4])    
