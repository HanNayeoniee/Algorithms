"""
백준 3009. 네번째 점
problem : https://www.acmicpc.net/problem/3009
"""

# 세 점의 좌표를 x, y 따로따로 리스트로 생성
x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)
    
# x, y리스트 안에 숫자가 1개인 값을 네번째 좌표로 설정
for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)
