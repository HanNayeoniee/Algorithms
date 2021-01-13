# 백준 8단계 2번 - 설탕 배달
# 5와 3을 최소 횟수로 합하여 N을 만드는 문제
# 5*x + 3*y = N

N = int(input())

x = list()  # 3kg 봉지의 개수
y = list()  # 5kg 봉지의 개수
result = 0

# 가능한 3kg, 5kg 봉지의 개수 구하기
for i in range(int(N/3)+1):
    for j in range(int(N/5)+1):
        if ((3*i + 5*j) ==N):
            x.append(i)
            y.append(j)

# 해당하는 경우가 없으면 -1
if not x:
    result = -1
# 5kg 봉지 개수가 가장 많은 경우 찾기
else:
    max = y[0]
    idx = 0
    for i in range(len(y)):
        if(max<y[i]):
            max = y[i]
    idx = y.index(max)
    result = x[idx] + y[idx]
print(result)