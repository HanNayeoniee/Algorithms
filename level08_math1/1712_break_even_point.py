# 백준 8단계 1번 - 손익분기점
# 고정비용, 가변비용, 판매가격이 주어졌을 때, 이익이 발생하는 판매량 수 구하기
# a+b*x < c*x 이므로 식을 정리하면, a/(c-b) < x이다.

a, b, c = list(map(int, input().split()))
break_even_point = 0

if (c <= b):
    break_even_point = -1
else:
    break_even_point = a // (c-b) + 1
print(break_even_point)