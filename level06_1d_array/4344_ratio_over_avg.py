# 백준 1차원 배열- 4344번: 평균은 넘겠지
# 평균을 넘은 학생들의 비율 구하기
# calculate how many students got better than an average


# 테스트 케이스의 개수 입력
n=int(input())
res=[]  # 평균을 넘는 학생의 비율

# 테스트 케이스만큼 반복
for i in range(n):
    avg=0
    ratio=0
    scores = list(map(int, input().split()))
    avg=sum(scores[1:])/(len(scores)-1)

    # 평균을 넘는 학생의 비율 구하기
    for i in range(1, len(scores), 1):
        if (scores[i]> avg):
            ratio+=1
    ratio=ratio/float(len(scores)-1)*100
    res.append(ratio)

# 평균을 넘는 학생들의 비율 출력
for i in range(n):
    print("%.3f%%" % res[i])
