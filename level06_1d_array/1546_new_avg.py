# 백준 1차원 배열- 1546번: 점수 바꿔치기한 평균 구하기

# 과목 개수, 점수 입력받기
n=int(input())  # 과목 개수
scores = list(map(int, input().split()))  # 과목 점수
# print(scores)

# 최댓값 구하기
Max=scores[0]
for i in range(n):
    if (scores[i]> Max):
        Max=scores[i]
# print(Max)

# 평균 다시 계산하기
avg=0
for i in range(n):
    scores[i]=scores[i]/Max*100
    avg+=scores[i]
avg=avg/n
print(avg)
