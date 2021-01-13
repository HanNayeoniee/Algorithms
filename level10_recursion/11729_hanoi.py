# 백준 10단계 4번 - 하노이 탑 이동 순서
# 재귀적인 패턴을 재귀함수로 찍는 문제 2

# 문제 설명:
# 원반꽂이 3개 start, tmp, end가 순서대로 있고
# 처음에 모든 원반은 start에 꽂혀있다.

# 내 풀이:
# 원반개수가 1인 경우에는 start->end 로 원반을 옮기고
# 나머지 경우에는 1) start의 맨 아래 원반을 제외한 원반을 tmp로 옮긴다.
#               2) start에 있는 원반 1개를 end로 옮긴다.
#               3) tmp에 있는 원반을 end로 옮긴다.

cnt = 0
def hanoi_tower(n, start, tmp, end):
    if (n==1):
        # print("원반 1을 {}에서 {}로 옮긴다.".format(start, end))
        print(start, end)
        global cnt
        cnt +=1
    else:
        hanoi_tower(n-1, start, end, tmp)
        # print("원반 {}을 {}에서 {}로 옮긴다.".format(n, start, end))
        print(start, end)
        cnt +=1
        hanoi_tower(n-1, tmp, start, end)
    return cnt

n = int(input())
print(2 ** n -1)
cnt = hanoi_tower(n, '1', '2', '3')