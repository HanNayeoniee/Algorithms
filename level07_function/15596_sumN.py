# 백준 함수- 15596번: 정수 N개의 합
# 정수 N개가 주어졌을 떄, N개의 합을 구하는 함수
# a는 합을 구해야 하는 정수 N개가 들어있는 리스트

def solve(a):
    ans=0
    for i in range(len(a)):
        ans+=a[i]
    return ans

# main
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
solve(a)
