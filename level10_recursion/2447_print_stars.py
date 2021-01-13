# 백준 10단계 3번 - 별 찍기
# 재귀적인 패턴을 재귀함수로 찍는 문제 1

import sys

def star(i, j):
    while (i != 0):
        # 몫이 1인 경우
        if(i%3 == 1 and j%3 ==1):
            sys.stdout.write(' ')
            return None
        i = i//3
        j = j//3
    sys.stdout.write('*')

n = int(input())
for i in range(n):
    for j in range(n):
        star(i, j)
    sys.stdout.write('\n')

